from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings


def home(request):
    return HttpResponse('Home page')


def contact(request):
    return HttpResponse('Contact page')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vox.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
