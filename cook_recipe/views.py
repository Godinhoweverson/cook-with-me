from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    return render(request, 'index.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': recipes})

def recipe_content(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_content.html', {'recipe': recipe})

def register(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')


