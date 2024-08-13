from django.shortcuts import render, redirect
from recipe.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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