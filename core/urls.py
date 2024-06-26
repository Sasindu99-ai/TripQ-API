from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import settings
from vvecon.zorion.urls import include

app_name = 'admin'

urlpatterns = [
    path('superadmin/', admin.site.urls),
    include('apps.main.urls'),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
