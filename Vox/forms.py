from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'quotes', 'postimg']


class UpdateProfileForm(forms.ModelForm):

    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'forms-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
