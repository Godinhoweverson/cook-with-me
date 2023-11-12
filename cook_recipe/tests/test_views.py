from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from cook_recipe.models import Recipe, Comment
from cook_recipe.forms import CommentForm


class RecipeViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
            )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            content='This is a test content for the recipe'
            )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')

    def test_recipe_content_view(self):
        response = self.client.get(reverse(
            'recipe_content',
            args=[self.recipe.id]
            ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_content.html')
        self.client.login(username='testuser', password='testpass123')
        form_data = {'content_body': 'Test comment content'}
        response = self.client.post(reverse(
            'recipe_content',
            args=[self.recipe.id]),
            form_data
             )
        self.assertEqual(response.status_code, 302)
        self.client.logout()
        response = self.client.post(reverse('recipe_content',
                                            args=[self.recipe.id]),
                                    form_data
                                    )
        self.assertEqual(response.status_code, 302)

    def test_recipe_content_view(self):
        response = self.client.get(reverse(
            'recipe_content',
            args=[self.recipe.id]
            ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_content.html')

    def test_recipe_content_view_form_invalid(self):
        response = self.client.post(reverse('recipe_content',
                                    args=[self.recipe.id]), {})
        self.assertEqual(response.status_code, 302)

    def test_recipe_like_view(self):
        response = self.client.get(reverse(
            'recipe_like', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertFalse(self.user in recipe.likes.all())

    def test_recipe_like_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse(
            'recipe_like',
            args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertTrue(self.user in recipe.likes.all())

    def test_recipe_like_view_no_referer(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('recipe_like',
                                   args=[self.recipe.id]), HTTP_REFERER='')
        self.assertEqual(response.status_code, 302)

    def test_edit_comment_view(self):
        comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            content_body='Test comment')
        response = self.client.get(reverse('edit_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'edit_comment.html')

        # Now, add test cases for the lines of code in the `edit_comment` view.
        self.client.login(username='testuser', password='testpass123')

        # Test the case where the user is allowed to edit the comment.
        form_data = {'content_body': 'Updated comment content'}
        response = self.client.post(reverse(
            'edit_comment', args=[comment.id]), form_data)
        self.assertEqual(response.status_code, 302)
        # Add assertions to check if the comment is updated.

        # Test the case where the user is not allowed to edit the comment.
        other_user = User.objects.create_user(
            username='otheruser', password='otherpass123')
        self.client.login(username='otheruser', password='otherpass123')
        response = self.client.post(reverse(
            'edit_comment', args=[comment.id]), form_data)
        self.assertEqual(response.status_code, 302)

    def test_edit_comment_view_user_allowed_to_edit(self):
        # Create a comment by the user
        comment = Comment.objects.create(
             recipe=self.recipe, user=self.user, content_body='Test comment')

        self.client.login(username='testuser', password='testpass123')

        # Test the case where the user is allowed to edit the comment.
        form_data = {'content_body': 'Updated comment content'}
        response = self.client.post(reverse(
            'edit_comment', args=[comment.id]), form_data)
        self.assertEqual(response.status_code, 302)
        updated_comment = Comment.objects.get(id=comment.id)
        self.assertEqual(updated_comment.content_body,
                         'Updated comment content')

    def test_edit_comment_view_user_not_allowed_to_edit(self):
        # Create a comment by the user
        comment = Comment.objects.create(
            recipe=self.recipe, user=self.user, content_body='Test comment')

        other_user = User.objects.create_user(
            username='otheruser', password='otherpass123')
        self.client.login(username='otheruser', password='otherpass123')

        # Test the case where the user is not allowed to edit the comment
        form_data = {'content_body': 'Updated comment content'}
        response = self.client.post(reverse(
            'edit_comment', args=[comment.id]), form_data)
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertNotEqual(comment.content_body, 'Updated comment content')

    def test_delete_comment_view(self):
        comment = Comment.objects.create(
            recipe=self.recipe, user=self.user, content_body='Test comment')
        response = self.client.get(reverse(
            'delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'delete_comment.html')

        # Now, add test cases for the lines of code
        # in the `delete_comment` view.
        self.client.login(username='testuser', password='testpass123')

        # Test the case where the user is allowed to delete the comment.
        response = self.client.post(reverse(
            'delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(
            id=comment.id).exists())  # Ensure the comment is deleted.

        # Test the case where the user is not allowed
        # to delete the comment (e.g., different user).
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass123')
        comment_by_other_user = Comment.objects.create(
            recipe=self.recipe,
            user=other_user,
            content_body='Other user comment'
        )
        response = self.client.post(reverse(
            'delete_comment',
            args=[comment_by_other_user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(
            id=comment_by_other_user.id).exists())
        # Ensure the comment is not deleted.

    def test_delete_comment_view_user_allowed_to_delete(self):
        # Create a comment by the user
        comment = Comment.objects.create(recipe=self.recipe,
                                         user=self.user,
                                         content_body='Test comment')

        self.client.login(username='testuser', password='testpass123')

        # Test the case where the user is allowed to delete the comment.
        response = self.client.post(reverse(
            'delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(
            id=comment.id).exists())  # Ensure the comment is deleted

    def test_delete_comment_view_user_not_allowed_to_delete(self):
        # Create a comment by the user
        comment = Comment.objects.create(
            recipe=self.recipe, user=self.user, content_body='Test comment')

        other_user = User.objects.create_user(
            username='otheruser', password='otherpass123')
        self.client.login(username='otheruser', password='otherpass123')

        # Test the case where the user is not allowed
        # to delete the comment (e.g., different user).
        response = self.client.post(reverse(
             'delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        # Ensure the response is a redirect
        comment.refresh_from_db()
        self.assertTrue(Comment.objects.filter(id=comment.id).exists())
        # Ensure the comment is not deleted

    def test_recipe_like_remove_like(self):
        # Create a recipe that the user has already liked
        self.recipe.likes.add(self.user)

        # Log in the user
        self.client.login(username='testuser', password='testpass123')

        # est that the user's like is removed when they access the view
        response = self.client.get(reverse(
            'recipe_like', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertFalse(self.user in recipe.likes.all())
