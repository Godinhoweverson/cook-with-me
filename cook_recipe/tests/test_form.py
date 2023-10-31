from django.test import TestCase
from cook_recipe.models import Recipe, Comment
from cook_recipe.forms import CommentForm, PasswordSignupForm


class CommentFormTest(TestCase):

    
    def test_form_meta_class(self):
        form = CommentForm()
        self.assertEqual(form.Meta.model, Comment)
        self.assertEqual(list(form.Meta.fields), ['content_body'])
    

    def test_valid_form(self):
        recipe = Recipe.objects.create(title='Test Recipe')
        data = {
            'content_body': 'This is a test comment',
            'recipe': recipe.id 
        }

        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())


    def test_invalid_form(self):
        data = {'content_body': ''}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())


    def test_form_save(self):
        recipe = Recipe.objects.create(title='Test Recipe')
        data = {
            'content_body': 'This is another test comment'
        }
        form = CommentForm(data=data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            self.assertEqual(comment.content_body, 'This is another test comment')
        else:
            self.fail('Form is not valid.')


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




    

