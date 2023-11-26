from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content','head_image','file_upload','category']

    def __init__(self, *args, **kwargs):
        # Get the user from the form's kwargs
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

        # Set the 'author' field to the current user
        if user:
            self.fields['author'].initial = user
            self.fields['author'].widget = forms.HiddenInput()
