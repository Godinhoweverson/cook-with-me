from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Recipe(models.Model):
    featured_image = CloudinaryField('image')
    title = models.CharField(max_length=150, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='recipes_likes', blank=True)

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()