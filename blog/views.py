from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})
def post_list_about(request):
	a = 'hello! Jango 1.10'
	return render(request, 'blog/post_list_about.html', {'a': a})
