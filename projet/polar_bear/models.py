from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    author = models.CharField(max_length=42)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    image = models.ImageField(upload_to='polar_bear/static/polar_bear/img/', null=True, blank=True) 
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)