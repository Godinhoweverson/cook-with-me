from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_date')
    list_filter = ('title', 'created_date')
    search_fields = ['title', 'created_date']
    summernote_fields = ('content', 'content_method')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('recipe', 'user', 'first_name', 'created_on', 'content_body', 'comment_approved')
    list_filter = ('recipe', 'user', 'created_on', 'email')
    search_fields = ['recipe', 'user', 'created_on']
    actions =['comment_approved']

    def comment_approved(self, request, queryset):
        queryset.update(approved=True)

# Register your models here.
