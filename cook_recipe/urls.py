from django.urls import path
from . import views
from django.conf.urls import handler500


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/<int:recipe_id>/',
         views.recipe_content,
         name='recipe_content'
         ),
    path('comment/edit/<int:comment_id>/',
         views.edit_comment,
         name='edit_comment'
         ),
    path('comment/delete/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'
         ),
    path('recipe/<int:recipe_id>/like/',
         views.recipe_like,
         name='recipe_like'),
    path('check_server_error', views.check_server_error, name= 'check_server_error')
]
handler500 = 'cook_recipe.views.error_500'
