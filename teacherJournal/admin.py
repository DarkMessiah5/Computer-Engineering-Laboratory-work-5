from django.contrib import admin
from .models import (
    Student
)
# Register your models here.

#class SubjectInline(admin.TabularInline):

admin.site.register(Student)

