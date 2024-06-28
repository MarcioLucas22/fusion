from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings # Esse import permite que busquemos informações do arquivo settings.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
