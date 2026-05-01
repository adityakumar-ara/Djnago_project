from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def clean(self):
        if not self.image and not self.video:
            raise ValidationError("Either image or video is required.")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['post', 'user']