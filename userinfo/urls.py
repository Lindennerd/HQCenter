from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_change

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^settings/$', 'userinfo.views.settings', name='user_settings'),
)
