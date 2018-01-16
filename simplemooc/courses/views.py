from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment, Announcements
from .forms import ContactCourse, CommentForm

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    template = 'courses/index.html'
    return render(request, template, context)

# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     context = {
#         'course': course
#     }
#     template = 'courses/details.html'
#     return render(request, template, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}

    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            print(form.cleaned_data)# retorna um dicionario com dados do form
            form = ContactCourse()
    else:
        form = ContactCourse()

    context['course'] = course
    context['form'] = form

    template = 'courses/details.html'
    return render(request, template, context)

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user,
                                                           course=course)
    if created:
        enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você ja está inscrito no curso')

    return redirect('accounts:dashboard')

@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Sua Inscrição foi cancelada com sucesso')
        return redirect('accounts:dashboard')
    context = {
        'enrollment': enrollment,
        'course': course,
    }
    template = 'courses/undo_enrollment.html'
    return render(request, template, context)

@login_required
def announcements(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        if not enrollment.is_approved():
            messages.error(request, 'A sua inscrição está pendente')
            return redirect('accounts:dashboard')
    context = {
        'course': course,
        'announcements': course.announcements.all(),
    }
    template = 'courses/announcements.html'
    return render(request, template, context)

@login_required
def show_announcement(request, slug, id):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        if not enrollment.is_approved():
            messages.error(request, 'A sua inscrição está pendente')
            return redirect('accounts:dashboard')

    announcement = get_object_or_404(course.announcements.all(), id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        messages.success(request, 'Seu comentário foi enviado com sucesso')

    context = {
        'course': course,
        'announcement': announcement,
        'form': form,
    }
    template = 'courses/show_announcement.html'
    return render(request, template, context)
