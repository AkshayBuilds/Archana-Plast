from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from home.models import *
from django.core.mail import send_mail
import smtplib
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        mobile = request.POST.get('number1')
        subject = request.POST.get('subject1')
        message = request.POST.get('message1')

        # Check if the necessary fields are filled
        if not name or not email or not mobile or not subject or not message:
            return render(request, 'contact.html', {'error': 'All fields are required.'})

        # Save data to the database
        try:
            data = save(name=name, email=email,mobile = mobile, subject=subject, message=message)
            data.save()
        except Exception as e:
            print(f"Error saving data: {e}")  # This will help identify issues
            return render(request, 'contact.html', {'error': 'There was an error saving your enquiry.'})
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('ishanpanchal202@gmail.com','hbaw pjbc lwnw mmle')  # Use app password here # for meet mail id
            server.login('amsp604@gmail.com','jmrf rkdj dpxo qnf')  # Use app password here #for ishan mail id
            message = f"Subject: {subject}\n\nFrom: {email} \n\nName: {name} \n\nMobile: {mobile} \n\nSubject: {subject}\n\nMessage:{message}"
            server.sendmail([email], 'ishanpanchal202@gmail.com', message) 
            server.sendmail([email], 'amsp604@gmail.com', message)
            server.quit()
            print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')

def service(request):
    return render(request, 'service.html')
