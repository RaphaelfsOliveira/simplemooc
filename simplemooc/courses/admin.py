from django.contrib import admin
from .models import Course

#opções para mostrar no painel do Django admin
class CourseAdmin(admin.ModelAdmin):

    #campos da classe que serão mostrados no Django_admin
    list_display = ['name', 'slug', 'start_date', 'created_at']
    #campo busca e campos que serão buscados no Django_admin
    search_fields = ['name', 'slug']
    #campo para preenchimento automatico para alguns campos
    prepopulated_fields = {'slug': ('name',)}

# Register your models here. e models Admin
admin.site.register(Course, CourseAdmin)
