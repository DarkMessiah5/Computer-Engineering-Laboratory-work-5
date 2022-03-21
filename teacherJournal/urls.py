from django.contrib import admin
from django.urls import path

from .views import Index, AddStudent, ChangeMark, student_data_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Index.as_view(), name='Index'),
    path('add_student/', AddStudent.as_view(), name='AddStudent'),
    path('change_student/', ChangeMark.as_view(), name='ChangeMark'),
    path('change_student/<int:pk>/', student_data_view, name='student-data')
]
