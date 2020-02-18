"""fast_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^bangla_newspaper/', views.bangla_news, name='bangla_newspaper'),
    url(r'^english_newspaper/', views.english_news, name='english_newspaper'),
    url(r'^news_channel/', views.news_channels, name='news_channel'),
    url(r'^note/', views.notes, name='note'),

]
