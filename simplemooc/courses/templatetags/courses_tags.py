from django.template import Library

register = Library()

from courses.models import Enrollment

@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context

@register.inclusion_tag('courses/templatetags/my_courses_details.html')
def my_courses_details(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context
