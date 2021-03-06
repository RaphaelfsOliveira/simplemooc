from django.contrib import admin
from .models import (Course, Enrollment, Announcements, Comment, Lesson, Material)

#opções para mostrar no painel do Django admin
class CourseAdmin(admin.ModelAdmin):

    #campos da classe que serão mostrados no Django_admin
    list_display = ['name', 'slug', 'start_date', 'created_at']
    #campo busca e campos que serão buscados no Django_admin
    search_fields = ['name', 'slug']
    #campo para preenchimento automatico para alguns campos
    prepopulated_fields = {'slug': ('name',)}


class EnrollmentAdmin(admin.ModelAdmin):

    list_display = ['course', 'user', 'status', 'created_at']


class MaterialInlineAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at'] # filtragem lateral

    inlines = [MaterialInlineAdmin]


# Register your models here. e models Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register([Announcements, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
