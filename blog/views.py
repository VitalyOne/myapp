from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User


# Create your views here.
def main_theme(request):
	#posts = Post.objects.order_by('-created_date')
	return render(request, 'blog/main.html', {})

def post_list(request):
	posts = Post.objects.order_by('-created_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
def post_list_about(request):
	a = 'hello! Jango 1.10'
	return render(request, 'blog/post_list_about.html', {'a': a})
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            else:
               
                post.author = User.objects.get(username='guest')
          
            
            
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_new.html', {'form': form})
