from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'body', 'head_image', 'price', 'place')
        labels = {
            'title': '제목 ',
            'body': '자세한 설명 ',
            'price': '가격 ',
            'head_image': '사진 첨부 ',
            'place': '만날 장소 '
        }
