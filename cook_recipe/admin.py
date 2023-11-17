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

    list_display = ('recipe', 'user', 'created_on',
                    'content_body', 'comment_approved')
    list_filter = ('recipe', 'user', 'created_on', 'email')
    search_fields = ['recipe', 'user', 'created_on']
    actions = ['comment_approved']

    def approve_comments(self, request, queryset):
        queryset.update(comment_approved=False)

    approve_comments.short_description = 'Approve selected comments'


