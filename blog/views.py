from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
	post = Post.objects.filter(published_Date__lte=timezone.now()).order_by('published_Date')
	return render(request, 'blog/post_list.html', {"posts": post})