from django.contrib import admin

from hub.models import Coach, MemberShip, Projet, Student

# Register your models here.
admin.site.register([Student,Coach,Projet,MemberShip])
