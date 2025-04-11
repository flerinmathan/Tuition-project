from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import FeePayment
from django.utils.timezone import now

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

def payment_tracking(request):
    # Get the current month and year
    current_month = now().strftime("%B %Y")  # e.g., "April 2025"

    # Fetch all payment records for the current month
    payments = FeePayment.objects.filter(month=current_month)

    return render(request, 'tuition_app/payment_tracking.html', {
        'payments': payments,
        'current_month': current_month,
    })

def mark_as_paid(request, payment_id):
    # Mark a specific payment as paid
    payment = get_object_or_404(FeePayment, id=payment_id)
    payment.is_paid = True
    payment.payment_date = now().date()  # Record the payment date
    payment.save()
    return redirect('payment_tracking')  # Redirect back to the tracking page