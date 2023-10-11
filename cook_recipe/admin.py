from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_date')
    list_filter = ('title', 'created_date')
    search_fields = ['title', 'created_date']
    summernote_fields = ('content')


# Register your models here.
