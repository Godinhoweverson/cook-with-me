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

    def test_approve_comments(self):
        # Create a comment with comment_approved=False
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
            comment_approved=True
        )

        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Select the comment for approval using the admin action
        response = self.client.post('/admin/cook_recipe/comment/', {
            '_selected_action': [str(comment.id)],
            'action': 'comment_approved',
        })

        # Check if the response is a successful redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Reload the comment from the database
        # to check if comment_approved is True
        reloaded_comment = Comment.objects.get(pk=comment.pk)
        self.assertTrue(reloaded_comment.comment_approved)
