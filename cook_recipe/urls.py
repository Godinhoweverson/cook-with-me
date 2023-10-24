from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipe_content, name='recipe_content'),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
]
