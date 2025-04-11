from django.urls import path
from . import views

urlpatterns = [
    path('student-registration/', views.student_registration, name='student_registration'),
    path('payment-tracking/', views.payment_tracking, name='payment_tracking'),
    path('mark-paid/<int:payment_id>/', views.mark_as_paid, name='mark_as_paid'),
    path('student-details/', views.student_details, name='student_details'),
]