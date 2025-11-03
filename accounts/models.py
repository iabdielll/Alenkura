from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        TEACHER = 'TEACHER', 'Docente'
        PROFESSIONAL = 'PROFESSIONAL', 'Profesional'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.TEACHER)
    cargo = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        full_name = self.get_full_name().strip()
        return full_name if full_name else self.username

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Roles.ADMIN
        super().save(*args, **kwargs)


class Course(models.Model):
    class Levels(models.TextChoices):
        BASIC = 'BASICO', 'Básico'
        LABORAL = 'LABORAL', 'Laboral'

    level = models.CharField(max_length=10, choices=Levels.choices, default=Levels.BASIC)
    name = models.CharField(max_length=150)
    year = models.PositiveSmallIntegerField()
    teachers = models.ManyToManyField('accounts.User', related_name='courses', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-year', 'name')

    def __str__(self) -> str:
        return f'{self.name} - {self.year}'
