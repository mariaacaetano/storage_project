from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customuser/', include('storage_customuser.urls')),
    path('storage_management/', include('storage_management.urls')),
]
