from django.test import TestCase
from django.contrib.auth.models import User
from cook_recipe.models import Recipe, Comment
from django.contrib import admin

class AdminTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_recipe_admin(self):
        recipe = Recipe.objects.create(
            title='Test Recipe',
            created_date='2023-01-01',
            content='Test content',
            content_method='Test content method'
        )

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/admin/cook-recipe/recipe/')
        self.assertEqual(response.status_code, 302)


    def test_comment_admin(self):
        comment = Comment.objects.create(
            recipe=Recipe.objects.create(
                title='Test Recipe',
                created_date='2023-01-01',
                content='Test content',
                content_method='Test content method'
            ),
            user=self.user,
            created_on='2023-01-01',
            content_body='Test comment body',
            comment_approved=False
        )

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/admin/cook_recipe/comment/')
        self.assertEqual(response.status_code, 302)


    def test_comment_approve_action(self):
        comment = Comment.objects.create(
            recipe=Recipe.objects.create(
                title='Test Recipe',
                created_date='2023-01-01',
                content='Test content',
                content_method='Test content method'
            ),
            user=self.user,
            created_on='2023-01-01',
            content_body='Test comment body',
            comment_approved=False
        )

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/admin/cook-with-me/comment/', {
            '_selected_action': [str(comment.id)],
            'action': 'approve_comments',
            'post': 'yes',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.get(pk=comment.pk).comment_approved, False)
