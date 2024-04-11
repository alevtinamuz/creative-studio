from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('account.urls')),
    path('api/canvases/', include('canvas.urls')),
    path('admin/', admin.site.urls),
]
