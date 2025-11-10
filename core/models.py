from django.db import models

# Create your models here.
class DateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Levels(models.TextChoices):
    BASIC = 'BASICO', 'Básico'
    LABORAL = 'LABORAL', 'Laboral'

class CourseName(DateTime):
    name = models.CharField(max_length=150, unique=True)
    level = models.CharField(max_length=10, choices=Levels.choices, default=Levels.BASIC)

    def __str__(self) -> str:
        return self.name
    
class Course(DateTime):
    level = models.CharField(max_length=10, choices=Levels.choices, default=Levels.BASIC)
    name = models.ForeignKey(CourseName, on_delete=models.CASCADE)
    teachers = models.ManyToManyField('accounts.User', related_name='courses', blank=True)

    class Meta:
        ordering = ('name__name',)

    def __str__(self) -> str:
        return f'{self.name} - {self.created_at.year}'
    
class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=64, null=True)
    category = models.CharField(max_length=10, choices=Levels.choices, default=Levels.BASIC)

    class Meta:
        unique_together = [('category', 'code')]

    def __str__(self) -> str:
        return self.name

class Axis(models.Model):
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='ejes')

    def __str__(self) -> str:
        return self.name