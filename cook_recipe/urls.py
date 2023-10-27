from django.urls import path
from .views import home, recipe_list, recipe_content

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipes'),
    path('recipes/<int:recipe_id>/',  recipe_content, name='recipe_content'),
]
