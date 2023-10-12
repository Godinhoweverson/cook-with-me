from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def recipe(request):
    return render(request, 'recipe.html')

def register(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')





