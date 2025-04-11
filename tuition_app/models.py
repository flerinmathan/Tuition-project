from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Auto-generated unique ID
    name = models.CharField(max_length=100)  # Student's name
    age = models.IntegerField()  # Student's age
    student_class = models.IntegerField(choices=[(i, f"Class {i}") for i in range(1, 11)])  # Dropdown for classes 1-10
    parent_contact = models.CharField(max_length=15)  # Parent/Guardian contact number

    def __str__(self):
        return f"{self.name} (Class {self.student_class})"
    
class FeePayment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)  # Link to Student model
    month = models.CharField(max_length=20)  # e.g., "April 2025"
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Fee amount
    is_paid = models.BooleanField(default=False)  # Payment status
    payment_date = models.DateField(null=True, blank=True)  # Date of payment (optional)

    def __str__(self):
        return f"{self.student.name} - {self.month} - {'Paid' if self.is_paid else 'Unpaid'}"