from django import forms
from .models import Post, Comment, Delivery

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content','head_image','file_upload','category','author']

    def __init__(self, *args, **kwargs):
        # Get the user from the form's kwargs
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['author'].initial = user
            self.fields['author'].widget = forms.HiddenInput()


class PostDelivery(forms.ModelForm):
    class Meta:
        model=Delivery
        fields=['title', 'content','head_image','file_upload','category','author']
        #widgets={'author':forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        user=kwargs.pop('user',None)
        super(PostDelivery, self).__init__(*args, **kwargs)

        if user:
            self.fields['author'].initial = user
            self.fields['author'].widget = forms.HiddenInput()

            #self.initial['author']=user
            #self.widget['author'] = forms.HiddenInput()


'''
    def __init__(self, *args, **kwargs):
        # Get the user from the form's kwargs
        #user = kwargs.pop('user', None)
        super(PostDelivery, self).__init__(*args, **kwargs)

        if user:
            self.fields['author'].initial = user
            self.fields['author'].widget = forms.HiddenInput()
'''