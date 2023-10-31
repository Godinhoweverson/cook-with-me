from .models import Comment
from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content_body',)


class PasswordSignupForm(SignupForm):
    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")

        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one digit.")

        return password



