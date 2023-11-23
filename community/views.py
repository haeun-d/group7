from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

def community_main(request):
    return render(request,'community/community_main.html')
def delivery(request):
    return render(request, 'community/delivery.html')
def food(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community/food.html', {'posts': posts})

#def food_post(request):
#    posts=Post.objects.all()
#    return render(request,'community/food.html',{'posts':posts})
#def delivery_post(request):
#    posts=Post.objects.all()
#    return render(request, 'community/delivery.html',{'posts':posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:food')
    else:
        form = PostForm()
    return render(request, 'community/create_post.html', {'form': form})

def food_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'community/food_detail.html', {'post': post})

def ott(request):
    return render(request, 'community/ott.html')

def search(request):
    query=request.GET.get('q')

    if query:
        posts=Post.objects.filter(title__icontains=query)
    else:
        if query:
            posts = Post.objects.filter(content__icontains=query)
        else:
            posts = []
    return render(request,'community/search_results.html',{'posts':posts, 'query':query})

def comment(request, pk):
    post=get_object_or_404(Post, pk=pk)
    comments=Comment.objects.filter(post=post)

    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.author=request.user
            new_comment.save()
            return redirect('community:food-detail', pk=pk)
        else:
            comment_form=CommentForm()
        return render(request, 'community/food_detail.html',{'post': post, 'comments':comments, 'comment_form':comment_form})


#class PostList(ListView):
#    model = Post
#    ordering = '-created_at'

#class PostDetail(DetailView):
#    model = Post