from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    featured_image = CloudinaryField('image')
    recipe_image = CloudinaryField('image', null=True, blank=True)
    title = models.CharField(max_length=150, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    content_method = models.TextField(default="Default content for method.")
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='recipes_likes',
        blank=True
    )

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    email = models.EmailField(max_length=50, blank=True, null=True)
    content_body = models.TextField(max_length=400)
    comment_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"Comment {self.content_body} by {self.user.username}"
        return f"Comment {self.content_body} by Anonymous"
