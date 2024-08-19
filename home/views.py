from django.shortcuts import render
from django.http import HttpResponse
from .utils import send_email_to_client, send_email_with_attachement
from django.conf import settings
from home.models import Car
import random

def home(request):
#  send_email_to_client()
#  subject = "This is django test mail"
#  message = "Hi Pavan, This is django test mail."
#  recipient_list = ["pkumarrathor@gmail.com"]
#  file_path = f"{settings.BASE_DIR}/test.txt"
#  send_email_with_attachement(subject, message, recipient_list, file_path)

# using Signals
#  Car.objects.create(car_name=f"Nexon-{random.randint(0,100)}")
 context = {'page':'Django | Home'}
 return render(request,"frontend/index.html", context)

def about(request):
 students = [
  {'name':'Pavan Kumar','email':'pk@gmail.com','phone':9536955038,'age':31},
  {'name':'Umesh Kumar','email':'ukgautam@gmail.com','phone':9557732575,'age':27},
  {'name':'Nitesh Kumar','email':'nitesh@gmail.com','phone':7834826128,'age':14},
  {'name':'Divyansh','email':'divyansh@gmail.com','phone':9536955038,'age':5},
 ]
 page = "Django | About us"
 return render(request, "frontend/about.html", context={'students': students, 'page': page})

def contact(request):
 context = {'page':'Django | Contact Us'}
 return render(request, "frontend/contact.html", context)

def message(request):
 return HttpResponse("this is success message")