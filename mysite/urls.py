"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, include

from rest_framework.documentation import include_docs_urls

# Admin Site Config
admin.sites.AdminSite.site_header = 'HDCiname Admin'
admin.sites.AdminSite.site_title = 'HDCiname Admin'
admin.sites.AdminSite.index_title = 'HDCiname Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('myapps.home.urls')),
    
    
    path('',include('myapps.api.urls')),
    
    path('docs/', include_docs_urls(title='Snippet API'))
]
