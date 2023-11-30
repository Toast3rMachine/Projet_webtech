# models.py de comment
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField(null=True)
    date = models.DateField(null=True)
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=90)

    def __str__(self):
        return f"Titre: {self.title}"

class Comment(models.Model):
    post = models.ForeignKey('comment.Post', on_delete=models.CASCADE, related_name='nouvelle_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=90)  # Ajoutez le champ title ici si nécessaire
    active = models.BooleanField(default=True)  # Ajoutez le champ active ici si nécessaire

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
