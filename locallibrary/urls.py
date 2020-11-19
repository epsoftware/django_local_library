"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include # Added per tutorial 
from django.views.generic import RedirectView # Added per tutorial
from django.conf import settings
from django.conf.urls.static import static

#Add URL maps to redirect the base URL to our application
# urlpatterns = [
# path('admin/', admin.site.urls),
# urlpatterns += [
#     path('catalog/', include('catalog.urls')),
# ]
# #from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='catalog/', permanent=True)),
# ]

# from .views import (main_page,
#                    contact_page,
#                    about_page)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('contact/', contact_page),
#     path('about/', about_page),
#     path('', main_page),
#]


urlpatterns = [
 #   path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),       # Add Django site authentication urls (for login, logout, password management)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Use static() to add url mapping to serve static files during development (only)
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

