from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import home
from upload.views import books
from upload.views import lifts
from upload.views import games

urlpatterns = [
    re_path(r'^$', home, name='upload'),
    path(r'^books', books, name='books'),
    path(r'^lifts', lifts, name='lifts'),
    path(r'^games', games, name='games')
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
