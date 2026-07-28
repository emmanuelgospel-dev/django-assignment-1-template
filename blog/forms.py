from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 10, 'placeholder': 'Write your post...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-file'}),
        }
