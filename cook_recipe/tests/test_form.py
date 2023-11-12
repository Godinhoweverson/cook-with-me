# Import necessary modules
from django.test import TestCase
from cook_recipe.models import Recipe, Comment
from cook_recipe.forms import CommentForm


# Define a test class for CommentForm
class CommentFormTest(TestCase):


    # Test the form's meta class
    def test_form_meta_class(self):
        form = CommentForm()
        # Check if the form's model matches the Comment model
        self.assertEqual(form.Meta.model, Comment)
        # Check if the form's fields include only 'content_body'
        self.assertEqual(list(form.Meta.fields), ['content_body'])
    
    # Test a valid form submission
    def test_valid_form(self):
        # Create a Recipe instance
        recipe = Recipe.objects.create(title='Test Recipe')
        # Define form data with content_bod and associated recipe
        data = {
            'content_body': 'This is a test comment',
            'recipe': recipe.id 
        }

        form = CommentForm(data=data)
        # Check if the form is valid
        self.assertTrue(form.is_valid())

    
    def test_invalid_form(self):
        data = {'content_body': ''}
        form = CommentForm(data=data)
        
        self.assertFalse(form.is_valid())

    
    def test_form_save(self): 
        # Create a Recipe instance 
        recipe = Recipe.objects.create(title='Test Recipe') 
        # Define form data with content_body 
        data = { 
            'content_body': 'This is another test comment' 
        } 
        form = CommentForm(data=data) 
        if form.is_valid(): 
            # Save the comment object without committing to the database 
            comment = form.save(commit=False) 
            comment.recipe = recipe 
            comment.save() 
            # Check if the content_body is correctly saved 
            self.assertEqual(comment.content_body, 'This is another test comment') 
        else: 
            form.save() 



    

