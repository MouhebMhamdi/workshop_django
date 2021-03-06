import email
from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField() #de base charfield

class Student(User):
    pass

class Coach(User):
    pass

class Projet(models.Model):
    project_name=models.CharField(max_length=50)
    dure=models.IntegerField()
    temps_allocated=models.IntegerField(validators=[MinValueValidator(1,"le temps min doit etre 1 heure")])
    besoin=models.TextField(max_length=250)
    description=models.TextField(max_length=250)
    isValid=models.BooleanField(default=False)
    creator=models.OneToOneField(Student,
        on_delete=models.CASCADE,
        related_name='creators'
    )
    supervisor=models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        related_name='supervisors'
    )
    membre=models.ManyToManyField(
        Student,
        #on_delete=models.CASCADE,
        through='MemberShip',
        related_name='membres'
    ) #classe intermediaire nommé memberShip

class MemberShip(models.Model):
    projet=models.ForeignKey(Projet,
        on_delete=models.CASCADE,
        related_name='projets'
        )
    student=models.ForeignKey(Student,
        on_delete=models.CASCADE,
        related_name='students'
        )

    temps_allocated_by_member=models.IntegerField(default=0)