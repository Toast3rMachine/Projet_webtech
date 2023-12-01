"""Forms for the comment app."""

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Form for user comments."""
    class Meta:
        model = Comment
        fields = ['content', 'date', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
