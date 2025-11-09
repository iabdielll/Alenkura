from django.contrib import admin
from .models import Course, Subject, CourseName, Axis
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'created_at', 'teachers_list')
    list_filter = ('name', 'level', 'teachers')
    search_fields = ('name__name', 'teachers__username', 'teachers__first_name', 'teachers__last_name')

    def teachers_list(self, obj):
        return ", ".join([t.get_full_name() or t.username for t in obj.teachers.all()])
    teachers_list.short_description = "Docentes"


@admin.register(CourseName)
class CourseNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category')
    search_fields = ('name', 'code')

@admin.register(Axis)
class AxisAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject__name')