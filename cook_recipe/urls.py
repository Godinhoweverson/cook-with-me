from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipe_content, name='recipe_content'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('recipe/<int:recipe_id>/like/', views.recipe_like, name='recipe_like'),
    path('account/signup/', views.PasswordSignupView.as_view(), name='account_signup' )
]