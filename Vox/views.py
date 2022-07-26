from django.shortcuts import render, redirect
from Vox.models import Post
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, postForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Vox/home.html')


@login_required(login_url='userlogin')
def post(request):
    
    user = request.user
    posts = postForm(initial = {'name':user})

    if request.method == 'POST':
        print(request)
        posts = postForm(request.POST, request.FILES)
        if posts.is_valid():
            posts.save()
        

    context = {
        'posts': posts
    }

    return render(request, 'Vox/Post.html', context)


def like(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    post.like.add(user)
    return redirect('feed')

def unlike(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    post.like.remove(user)
    return redirect('feed')

def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('userlogin')

    context = {'form': form}
    return render(request, 'Vox/registration.html', context)


def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #messages.info(request, f"You are now logged in as {username}")
            return redirect('feed')
        else:
            #messages.info(request, "Username OR Password is incorrect")
            return redirect('userlogin')

    context = {}
    return render(request, 'Vox/userlogin.html', context)


def userlogout(request):
    logout(request)
    # messages.info(request, "Successfully logged out")
    print("logged out")
    return redirect('home')


@login_required(login_url='userlogin')
def feed(request):
    form = Post.objects.all()
    context = {'form': form}
    return render(request, 'Vox/feed.html', context)


@login_required
def profile(request):
    user = request.user
    form = user.profile
    posts = Post.objects.filter(name = user)
    context = {'form':form, 'posts': posts}
    
    return render(request, 'Vox/profile.html', context)