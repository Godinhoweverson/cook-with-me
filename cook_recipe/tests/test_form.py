#Import necessary modules
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

    # Test an invalid form submission (missing content_body)
    def test_invalid_form(self):
        data = {'content_body': ''}
        form = CommentForm(data=data)
        # Check if the form is not valid
        self.assertFalse(form.is_valid())

    # Test saving the form data
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
            self.fail('Form is not valid.')

    
# Tests for check password validation rules.
# It tests valid passwords, short passwords, missign uppercase letters, missing lowercase letters, and missing digits.
# The tests check if the form correctly identifies these issues and reports appropriate error messages.
class PasswordSignupFormTest(TestCase):
    def test_valid_password(self):
        # Create a form with a valid password
        form = PasswordSignupForm(data={'password1': 'ValidPassword123'})
        self.assertFalse(form.is_valid())
    

    def test_short_password(self):
        # Create a form with a password that is too short
        form = PasswordSignupForm(data={'password1': 'Short'})
        self.assertFalse(form.is_valid())
        self.assertIn('Password must be at least 8 characters long.', form.errors['password1'])


    def test_no_uppercase_letter(self):
        # Create a form with a password that lacks an uppercase letter
        form = PasswordSignupForm(data={'password1': 'nouppercase123'})
        self.assertFalse(form.is_valid())
        self.assertIn('Password must contain at least one uppercase letter.', form.errors['password1'])


    def test_no_lowercase_letter(self):
        # Create a form with a password that lacks an lowercase letter
        form = PasswordSignupForm(data={'password1': 'NOLOWERCASE123'})
        self.assertFalse(form.is_valid())
        self.assertIn('Password must contain at least one lowercase letter.', form.errors['password1'])


    def test_no_digit(self):
        # Create a form with a password that lacks a digit
        form = PasswordSignupForm(data={'password1': 'NoDigitPassword'})
        self.assertFalse(form.is_valid())
        self.assertIn('Password must contain at least one digit.', form.errors['password1'])




    

