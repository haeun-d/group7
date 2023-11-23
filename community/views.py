from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import PostForm
# Create your views here.
def community_main(request):
    return render(request,'community/community_main.html')
def delivery(request):
    return render(request, 'community/delivery.html')
def food(request):
    return render(request, 'community/food.html')

def food_post(request):
    posts=Post.objects.all()
    return render(request,'community/food.html',{'posts':posts})
def delivery_post(request):
    posts=Post.objects.all()
    return render(request, 'community/delivery.html',{'posts':posts})
def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:food')
    else:
        form=PostForm()
    return render(request, 'community/create_post.html',{'form':form})

def ott(request):
    return render(request, 'community/ott.html')

def search(request):
    query=request.GET.get('q')

    if query:
        posts=Post.objects.filter(title__icontains=query)
    else:
        if query:
            posts = Post.objects.filter(title__icontains=query)
        else:
            posts = []
    return render(request,'community/search_results.html',{'posts':posts, 'query':query})
class PostList(ListView):
    model = Post
    ordering = '-created_at'

class PostDetail(DetailView):
    model = Post