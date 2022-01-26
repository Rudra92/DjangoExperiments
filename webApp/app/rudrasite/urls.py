"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include

from .views import (home_page, about_page, contact_page)
from blog.views import (
    blogpost_create_view,
    )

from markdownx import urls as markdownx




urlpatterns = [
    #extensions

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    re_path(r'markdownx/', include(markdownx)),


    path('', home_page, name='home'),
    re_path(r'about/', about_page),
    re_path(r'contact/', contact_page),


    # blog
    re_path(r'blog/', include("blog.urls")),
    path('blog-create/', blogpost_create_view),





]
