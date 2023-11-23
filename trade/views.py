from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def trade_first(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'trade/trade_first.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trade:trade')
    else:
        form = PostForm()
    return render(request, 'trade/trade_write.html', {'form': form})

def trade_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'trade/trade_detail.html', {'post': post})
