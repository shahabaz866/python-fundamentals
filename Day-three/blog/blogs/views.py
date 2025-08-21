from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # fetch all posts (latest first)
    return render(request, 'blogs/post_list.html', {'posts': posts})
