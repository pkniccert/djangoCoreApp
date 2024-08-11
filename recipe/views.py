from django.shortcuts import render, redirect
from recipe.models import *
# Create your views here.

def addRecipe(request):
    # Recipe.objects.all().delete()
    context = {'page':'Django | Recipe'}
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
    return render(request, "recipe.html", context)
