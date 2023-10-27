from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': recipes})

@login_required
def recipe_content(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            return redirect('recipe_content', recipe_id=recipe.id)
    else:
        form = CommentForm()
    return render(request, 'recipe_content.html', {'form':form, 'recipe':recipe})





