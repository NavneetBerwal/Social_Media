from django.shortcuts import render, redirect
from Vox.models import Post
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'Vox/home.html')


def post(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quotes = request.POST.get('quotes')
        caption = request.POST.get('caption')
        post = Post(name=name, quotes=quotes,
                    caption=caption, date=datetime.today())
        post.save()

    return render(request, 'Vox/Post.html')


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            return redirect('home')

    context = {'form': form}
    return render(request, 'Vox/registration.html', context)


def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.info(request, "Username OR Password is incorrect")

    context = {}
    return render(request, 'Vox/userlogin.html', context)


def userlogout(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect('home.html')