from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('cook_recipe.urls'), name='cook_recipe.urls'),
    path("accounts/", include("allauth.urls")),
  
]