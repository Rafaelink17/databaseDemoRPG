from django.contrib import admin
from django.urls import path, include
from dataadministrator.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('dataadministrator/', include('dataadministrator.urls')),
]
