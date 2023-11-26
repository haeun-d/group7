from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from users.models import User

def trade_first(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'trade/trade_first.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('trade:trade')
    else:
        form = PostForm()
    return render(request, 'trade/trade_write.html', {'form': form})

def trade_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'trade/trade_detail.html', {'post': post})

def delete_post(request, pk):
    record=get_object_or_404(Post, pk=pk)
    record.delete()
    return redirect('trade:trade', request.user.username)

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 현재 사용자가 글의 작성자인지 확인
    if request.user != post.author:
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('trade:trade_detail', pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'trade/trade_write.html', {'form': form})
