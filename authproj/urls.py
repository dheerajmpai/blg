"""authproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views
from urlapp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('allauth.urls')),
#    url(r'^accounts/', include('allauth.urls')),
    path('', views.hello, name = 'home'),
    path('article/<slug:nn>', views.art ),    
    path('nopage/', views.my_view ),
    path('form/', v2.get_name),
    path('thanks/', v2.thank_view),
    path('write/', v2.get_article)
]


