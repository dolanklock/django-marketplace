from django.contrib import admin
from django.urls import path, include
# need to import the two below to get image to show
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this will allow images to be shown
