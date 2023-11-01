from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from cook_recipe.models import Recipe, Comment
from cook_recipe.forms import CommentForm

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.recipe = Recipe.objects.create(title='Test Recipe', content='This is a test content for the recipe')
    

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')

    
    def test_recipe_content_view(self):
        response = self.client.get(reverse('recipe_content', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_content.html')

    
    def test_recipe_content_view(self):
        response = self.client.get(reverse('recipe_content', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_content.html')
    

    def test_recipe_like_view(self):
        response = self.client.get(reverse('recipe_like', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)

    
    def test_recipe_like_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('recipe_like', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)


    def test_recipe_like_view_no_referer(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('recipe_like', args=[self.recipe.id]), HTTP_REFERER='')
        self.assertEqual(response.status_code, 302)


    def test_edit_comment_view(self):
        comment = Comment.objects.create(recipe=self.recipe, user=self.user, content_body='Test comment')
        response = self.client.get(reverse('edit_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_comment.html')


        def test_delete_comment_view(self):
        comment = Comment.objects.create(recipe=self.recipe, user=self.user, content_body='Test comment')
        response = self.client.get(reverse('delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_comment.html')