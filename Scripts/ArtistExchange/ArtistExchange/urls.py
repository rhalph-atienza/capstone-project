# Main urls file for the Django project

from django.contrib import admin
from django.urls import re_path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('main.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)