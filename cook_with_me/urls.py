from django.contrib import admin
from django.urls import path, include
from cook_recipe.views import home, recipe_list, register, login_page
from cook_recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', home, name='home'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipe_content, name='recipe_content'),
    path('register/', register, name='register'),
    path('login_page/', login_page, name='login_page'),

]