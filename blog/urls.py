from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .settings import MEDIA_ROOT, STATIC_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
