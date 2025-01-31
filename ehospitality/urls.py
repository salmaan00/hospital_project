"""ehospitality URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from doctor.views import*
from admin_app.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('admins/', include('admin_app.urls')),
    path('doctors/', include('doctor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
    path('admin-login/', AdminLoginView.as_view(), name='admin_login'),

    # Add this line for authentication
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

