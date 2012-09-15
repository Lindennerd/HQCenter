#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^signup/$', 'accounts.views.signup', name='signup'),

	url(r'^login/$', "django.contrib.auth.views.login",
        {'template_name': 'login.html'}, name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout',
    	{'next_page': '/'},name='logout'),

    url(r'^login_required/', 'django.views.generic.simple.direct_to_template', 
    		{'template' : 'invalid.html'}, name="login_required"),
)