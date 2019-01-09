from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=[
            'title',
            'category',
            'description',
            'author',
            'image',
        ]


class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=[
            'name',
            'comment',

        ]        