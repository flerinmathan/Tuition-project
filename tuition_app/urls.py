from django.urls import path
from . import views

urlpatterns = [
    path('student-registration/', views.student_registration, name='student_registration'),
]