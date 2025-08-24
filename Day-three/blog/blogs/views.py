from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm,SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def post_list(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogs/post_list.html', {'posts': posts})
@never_cache
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})
@never_cache
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blogs/post_form.html', {'form': form})
@never_cache
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_form.html', {'form': form})
@never_cache
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blogs/post_confirm_delete.html', {'post': post})
@never_cache
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'blogs/signup.html', {'form': form})