from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    price = models.CharField(max_length=50)
    head_image = models.ImageField(upload_to='trade/images/%Y/%m/%d/', blank=True)
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    allowed_reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='allowed_reviews')

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    def get_absolute_url(self):
        return f'/trade/{self.pk}/'

class ChatRoom(models.Model):
    post=models.ForeignKey(Post, related_name="chat", on_delete=models.CASCADE)
    buyer=models.ForeignKey(User, related_name='buyer',on_delete=models.CASCADE)
    seller=models.ForeignKey(User, related_name='seller',on_delete=models.CASCADE)

class Chatting(models.Model):
    chat_room=models.ForeignKey(ChatRoom, related_name="chat_room", on_delete=models.CASCADE )
    text=models.CharField(max_length=100)
    writer=models.ForeignKey(User, related_name='chatting_writer',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # 1에서 5까지의 평가를 가정합니다.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reviewer}님의 {self.post.title}에 대한 후기'
