from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CourseForm, UserCreateForm
from .models import Course

User = get_user_model()


@login_required
def dashboard(request):
    """Redirect users to the dashboard that matches their role."""
    if request.user.role == User.Roles.ADMIN:
        return redirect('admin_dashboard')
    return redirect('teacher_dashboard')


@login_required
def admin_dashboard(request):
    if request.user.role != User.Roles.ADMIN:
        return redirect('teacher_dashboard')

    active_panel = 'users'
    course_view = 'list'
    user_form = UserCreateForm()
    course_form = CourseForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type', 'user')
        if form_type == 'course':
            course_form = CourseForm(request.POST)
            active_panel = 'courses'
            course_view = 'form'
            if course_form.is_valid():
                course = course_form.save()
                messages.success(request, f'Curso {course.name} creado correctamente.')
                return redirect('admin_dashboard')
            messages.error(request, 'No pudimos crear el curso, revisa los campos resaltados.')
        else:
            user_form = UserCreateForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save()
                messages.success(request, f'Usuario {new_user.username} creado correctamente.')
                return redirect('admin_dashboard')
            messages.error(request, 'Revisa los campos marcados en rojo.')

    if course_form.errors:
        active_panel = 'courses'
        course_view = 'form'

    users = User.objects.order_by('first_name', 'username')
    courses = Course.objects.prefetch_related('teachers').all()

    return render(
        request,
        'accounts/admin_dashboard.html',
        {
            'user_form': user_form,
            'course_form': course_form,
            'users': users,
            'courses': courses,
            'active_panel': active_panel,
            'course_view': course_view,
            'show_user_modal': bool(user_form.errors),
        },
    )


@login_required
def teacher_dashboard(request):
    if request.user.role == User.Roles.ADMIN:
        return redirect('admin_dashboard')

    courses = Course.objects.prefetch_related('teachers').all()

    return render(
        request,
        'accounts/teacher_dashboard.html',
        {
            'user_role': request.user.get_role_display(),
            'courses': courses,
        },
    )
