from django.shortcuts import render, redirect
from recipe.models import *
from django.http import HttpResponse
# Create your views here.

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

def delete_recipe(request, id):
   queryset = Recipe.objects.get(id = id)
   queryset.delete()
   return redirect('/recipe/')

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