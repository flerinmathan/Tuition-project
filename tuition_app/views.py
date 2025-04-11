from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

def student_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        student_class = request.POST.get('student_class')
        parent_contact = request.POST.get('parent_contact')

        # Save the student to the database
        Student.objects.create(
            name=name,
            age=age,
            student_class=student_class,
            parent_contact=parent_contact
        )
        messages.success(request, "Student registered successfully!")
        return redirect('student_registration')

    # Pass the range for classes (1 to 10) to the template
    return render(request, 'tuition_app/student_registration.html', {
        'class_range': range(1, 11)
    })