from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from core.models import Course, Levels

User = get_user_model()

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre completo', max_length=150)
    role = forms.ChoiceField(label='Rol', choices=User.Roles.choices)
    cargo = forms.CharField(label='Cargo', max_length=150, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'role', 'cargo')

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.role = self.cleaned_data['role']
        user.cargo = self.cleaned_data['cargo']
        if commit:
            user.save()
        return user


class CourseForm(forms.ModelForm):
    level = forms.ChoiceField(label='Nivel', choices=Levels.choices)
    year = forms.IntegerField(label='Año', min_value=1900, max_value=2100)
    teachers = forms.ModelMultipleChoiceField(
        label='Docentes',
        queryset=User.objects.none(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': 6}),
        help_text='Selecciona uno o varios docentes responsables.',
    )

    class Meta:
        model = Course
        fields = ('name', 'level', 'year', 'teachers')
        labels = {
            'name': 'Nombre del curso',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teachers'].queryset = User.objects.filter(
            role__in=[User.Roles.TEACHER, User.Roles.PROFESSIONAL]
        ).order_by('first_name', 'username')