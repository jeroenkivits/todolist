from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

def todo_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todolistapp/todo_page.html', {'posts': posts})

def todo_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'todolistapp/todo_detail.html', {'post': post})

def todo_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'todolistapp/todo_edit.html', {'form': form})

def todo_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'todolistapp/todo_edit.html', {'form': form})

def weather(request):
    return render(request, 'todolistapp/weather.html')

def index(request):
    return render(request, 'todolistapp/index.html',)

def about(request):
    return render(request, 'todolistapp/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todolistapp/signup.html', {'form': form})

def login(request):
    return render(request, 'todolistapp/todo_page.html')

def logout(request):
    logout(request)
    return render(request, 'todolistapp/registration/logged_out.html')

def logout_view(request):
    logout(request)
    return redirect('todolistapp/index.html')
