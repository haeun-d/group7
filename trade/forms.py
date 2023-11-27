from django import forms
from .models import Post, Review


class PostForm(forms.ModelForm):
    allowed_reviewer_text = forms.CharField(required=False)
    class Meta:
        model=Post
        fields=('title', 'body', 'head_image', 'price', 'place', 'allowed_reviewer_text')
        labels = {
            'title': '제목 ',
            'body': '자세한 설명 ',
            'price': '가격 ',
            'head_image': '사진 첨부 ',
            'place': '만날 장소 ',
            'allowed_reviewer': '후기 작성 대상 닉네임',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        labels = {
            'text': '후기 내용',
            'rating': '평가',
        }
