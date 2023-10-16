from django.test import TestCase
from django.contrib.auth.models import User
from cook_recipe.models import Recipe, Comment

class RecipeModelTest(TestCase):


    def setup(self):
        # create a user fo test
        self.user1 = User.objects.create_user(username='testuser1', password='testpass123')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass456')

        # create a recipe for test
        self.recipe = Recipe.objects.create(
            title = 'Test Recipe',
            content = 'This is a test content for the recipe.'
        )


    def test_recipe_creation(self):
        #Checked if the recipe was created correctly 
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.content, 'This is test to verify if the content for recipe was created'
        
        )

    
    def test_recipe_str_representation(self):
        #verify the string representation
        self.assertEqual(str(self.recipe), 'Test Recipe')


    def test_number_of_likes(self):
        # In the begin the recipe does't have likes
        self.asserEqual(self.recipe.number_of_likes(), 0)

        # Add like 
        self.recipe.likes.add(self.user1)
        self.assertEqual(self.recipe.numner_of_likes(), 1)

        # Add other likes

             # Added likes
        self.recipe.likes.add(self.user2)
        self.assertEqual(self.recipe.numner_of_likes(), 2)


    