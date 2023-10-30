from django.test import TestCase
from cook_recipe.models import Recipe, Comment
from cook_recipe.forms import CommentForm


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
