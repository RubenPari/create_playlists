from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_flow/', include('auth_flow.urls')),
    path('playlists/', include('playlists.urls')),
]
