"""Forms for the comment app."""

from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    """Form for user comments."""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ArticleForm(forms.ModelForm):
    """Form for articles."""
    class Meta:
        model = Article
        fields = ['title', 'content']
