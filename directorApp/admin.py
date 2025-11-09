from django.contrib import admin
from .models import Parent, Student
# Register your models here.
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'phone')
    search_fields = ('first_name', 'email')
    list_filter = ('created_at', 'updated_at')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'rut', 'grade', 'curso', 'nivel')
    search_fields = ('first_name', 'rut')
    list_filter = ('grade', 'nivel', 'created_at', 'updated_at')
