from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Includes all URL patterns from the app1/urls.py file at the root level
    path('', include('app1.urls')),
]
