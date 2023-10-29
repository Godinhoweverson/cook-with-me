from django.urls import path
from .views import home, recipe_list, recipe_content, edit_comment, delete_comment

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipes'),
    path('recipes/<int:recipe_id>/', recipe_content, name='recipe_content'),
    path('comment/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]