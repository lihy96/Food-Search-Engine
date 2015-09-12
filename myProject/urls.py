"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from myFoodSearch.views import *
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^home/$', showMainTitle),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'd:/xiaoxueqi/myProject/myFoodSearch/static'}),
    url(r'^$','myFoodSearch.views.search',name='search'),
    # url(r'(\d+).html^$','myFoodSearch.views.openhtml',name='openhtml'),
    url(r'^search/?$', 'myFoodSearch.views.searched', name='searched'),
    url(r'^search/$','myFoodSearch.views.searched',name='searched'),
    url(r'^user/$', 'myFoodSearch.views.openhtml'),
    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += patterns{'',
#     url(r'^home/$', showMainTitle),
# }