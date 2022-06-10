from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page')


def contact(request):
    return HttpResponse('Contact page')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vox.urls')),
]
