from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from courses.models import Enrollment
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

# Create your views here.
@login_required
def dashboard(request):
    context = {}
    context['enrollments'] = Enrollment.objects.filter(user=request.user)
    template = 'accounts/dashboard.html'
    return render(request, template, context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    template = 'accounts/register.html'
    return render(request, template, context)

def password_reset(request):
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    template = 'accounts/password_reset.html'
    return render(request, template, context)

def password_reset_confirm(request, key):
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    template = 'accounts/password_reset_confirm.html'
    return render(request, template, context)

@login_required
def edit(request):
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados da sua conta foram alterados com sucesso')
            return redirect('accounts:dashboard')
    else:
        form = EditAccountForm(instance=request.user)

    context['form'] = form
    template = 'accounts/edit.html'
    return render(request, template, context)

@login_required
def edit_password(request):
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)

    context['form'] = form
    template = 'accounts/edit_password.html'
    return render(request, template, context)
