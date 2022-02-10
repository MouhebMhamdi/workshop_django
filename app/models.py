from pydoc import describe
from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField() 

    class Meta:
        verbose_name_plural="Categories"

class CLient(models.Model):
    first_name=models.CharField(max_length=50)
    dob=models.DateField()
    age=models.IntegerField(default=0)
    created_at=models.DateField(auto_now_add=True,null=True)
    modified_at=models.DateField(auto_now=True,null=True)
    description=models.TextField(null=True)


    Category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural="Clients"


