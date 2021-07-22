from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('movies_api.urls')),
    path('admin/', admin.site.urls),
]
