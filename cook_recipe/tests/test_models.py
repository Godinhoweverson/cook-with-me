from django.test import TestCase
from django.contrib.auth.models import User
from cook_recipe.models import Recipe

class RecipeModelTest(TestCase):

    def setUp(self):  
        self.user1 = User.objects.create_user(username='testuser1', password='testpass123')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass456')

        
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            content='This is a test content for the recipe.'
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.content, 'This is a test content for the recipe.') 

    def test_recipe_str_representation(self):
        self.assertEqual(str(self.recipe), 'Test Recipe')

    def test_number_of_likes(self):
        self.assertEqual(self.recipe.number_of_likes(), 0)
        self.recipe.likes.add(self.user1)
        self.assertEqual(self.recipe.number_of_likes(), 1)
        self.recipe.likes.add(self.user2)
        self.assertEqual(self.recipe.number_of_likes(), 2)
