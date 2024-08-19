from django.shortcuts import render, redirect
from recipe.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

@login_required(login_url="/login/")
def addRecipe(request):
    
    if request.method == "POST" :
     data = request.POST
     image = request.FILES.get('file')
     name = data.get('name')
     description = data.get('description')
     Recipe.objects.create(
      recipe_name=name,
      recipe_descrition=description,
      recipe_image=image
     )
     return redirect('/recipe/')
    #  print(name, description, image)
    recipes = Recipe.objects.all()

    if request.GET.get('search'):
       recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'page':'Django Recipe','recipes':recipes}
    return render(request, "recipe.html", context)

@login_required(login_url="/login/")
def delete_recipe(request, id):
   queryset = Recipe.objects.get(id = id)
   queryset.delete()
   return redirect('/recipe/')

@login_required(login_url="/login/")
def update_recipe(request, id):
   queryset = Recipe.objects.get(id = id)
   if request.method == "POST" :
     data = request.POST
     image = request.FILES.get('file')
     name = data.get('name')
     description = data.get('description')
     queryset.recipe_name = name
     queryset.recipe_descrition = description
     if image:
        queryset.recipe_image = image

     queryset.save()
     return redirect('/recipe/')
   
   context = {'page':'Django Recipe','recipe':queryset}
   return render(request, "update_recipe.html", context)

def login_page(request):
   if request.method == "POST":
      username=request.POST.get('username')
      password=request.POST.get('password')

      if not User.objects.filter(username = username).exists():
         messages.error(request, "Invalid Username.")
         return redirect('/login/')
      
      user = authenticate(username = username, password = password)
      if user is None:
         messages.error(request, "Invalid password.")
         return redirect('/login/')
      else:
         login(request, user)
         return redirect('/recipe/')
      

      messages.error(request, "Account Create Successfully.")
      return redirect('/register/')
    
   context = {'page':'Django Login Page'}
   return render(request, 'login.html', context)

def register_page(request):
   if request.method == "POST":
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')

      user = User.objects.filter(username = username)

      if user.exists():
         messages.error(request, "Username already taken.")
         return redirect('/register/')

      user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email 
      )

      user.set_password(password)
      user.save()
      messages.error(request, "Account Create Successfully.")
      return redirect('/register/')

   context = {'page':'Django Register Page'}
   return render(request, 'register.html', context)

def logout_page(request):
   logout(request)
   return redirect('/login/')

def get_students(request):
   queryset = Student.objects.all()
   if request.GET.get('search'):
       search = request.GET.get('search')
       queryset = queryset.filter(
          Q(name__icontains = search) |
          Q(email__icontains = search) |
          Q(phone__icontains = search) |
          Q(age__icontains = search) |
          Q(department__department__icontains = search) |
          Q(student_id__student_id__icontains = search)
          )
   paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
   page_number = request.GET.get("page",1)
   page_obj = paginator.get_page(page_number)
   context = {'page':'Django Students Data', 'students':page_obj}
   return render(request, 'report/students.html', context)

def see_marks(request, student_id):
   queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
   total_marks = queryset.aggregate(total_marks = Sum('marks'))
   context = {'page':'Django Student Marks', 'marks':queryset, 'total_marks':total_marks}
   return render(request, 'report/student_marks.html', context)