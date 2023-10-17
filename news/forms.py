from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'heading',
            'text',
            'post_category',
            'author'
        ]

        labels = {
            'heading': 'Title',
            'text': 'Text',
            'post_category': 'Category',
            'author': 'Author'
        }