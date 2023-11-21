from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def trade_first(request):
    return render(request, 'trade/trade_first.html')

def home(request):
    posts = Post.objects
    return render(request, 'trade/trade_first.html', {'posts' : posts})

def new(request):
    return render(request, 'trade/trade_write.html')

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')
