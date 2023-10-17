from django.test import TestCase
from django.contrib.auth.models import User
from cook_recipe.models import Recipe, Comment

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


class CommentModelTest(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(
            username = 'testuser',
            password = 'testpass123'
        )

        self.recipe = Recipe.objects.create(
            title = 'Test Recipe'
        )

        self.comment = Comment.objects.create(
            recipe = self.recipe,
            user = self.user,
            content_body = 'This is a test comment.',
        )

    def test_comment_creation(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.content_body, 'This is a test comment.')

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'Comment This is a test comment. by testuser')

    def test_comment_without_user(self):
        comment_without_user = Comment.objects.create(
            recipe = self.recipe,
            first_name = "John",
            last_name = "Doe",
            email = "john.doe@example.com",
            content_body =  "Another test comment."
        )
        self.assertEqual(str(comment_without_user), 'Comment Another test comment. by John')

