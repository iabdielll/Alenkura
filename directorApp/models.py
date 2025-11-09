from django.db import models
from core.models import DateTime, Course, Levels

# Create your models here.
class CollegeLevels(models.TextChoices):
    BASICO_COMPLETO = 'Básico Completo', 'Básico Completo'
    BASICO_INCOMPLETO = 'Básico Incompleto', 'Básico Incompleto'
    MEDIO_COMPLETO = 'Medio Completo', 'Medio Completo'
    MEDIO_INCOMPLETO = 'Medio Incompleto', 'Medio Incompleto'
    SUPERIOR = 'Superior', 'Superior'

class Parent(DateTime):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    rut = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=20)
    collage_level = models.CharField(max_length=20, choices=CollegeLevels.choices, default=CollegeLevels.BASICO_COMPLETO)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Student(DateTime):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    rut = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    bapDiag = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    commune = models.CharField(max_length=40)
    grade = models.CharField(max_length=40)
    etnia = models.CharField(max_length=40, null=True, blank=True)

    parents = models.ManyToManyField(Parent, related_name='students', blank=True)
    curso = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    nivel = models.CharField(max_length=10, choices=Levels.choices, default=Levels.BASIC)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.parents} {self.curso} {self.nivel}'