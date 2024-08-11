from django.shortcuts import render

from django.http import HttpResponse

def home(request):
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