# forms.py de comment
from django import forms
from .models import Post, Article, Comment

class MyCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
