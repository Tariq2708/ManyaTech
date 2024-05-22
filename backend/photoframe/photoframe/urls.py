from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),             # URL for the admin interface
    path('api/', include('frames.urls')),        # Including the URLs from the 'frames' app for API endpoints
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Serving media files during development
