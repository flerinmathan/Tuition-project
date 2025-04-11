from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Auto-generated unique ID
    name = models.CharField(max_length=100)  # Student's name
    age = models.IntegerField()  # Student's age
    student_class = models.IntegerField(choices=[(i, f"Class {i}") for i in range(1, 11)])  # Dropdown for classes 1-10
    parent_contact = models.CharField(max_length=15)  # Parent/Guardian contact number

    def __str__(self):
        return f"{self.name} (Class {self.student_class})"