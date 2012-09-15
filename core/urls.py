from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^ver/(?P<id>\d+)', 'core.views.details', name="details"),

    # ------ CRUD ----------
    #url(r'^novo/', 'core.views.create_comic', name="create_comic"),
    url(r'^editar/(?P<id>\d+)', 'core.views.update_comic', name="update_comic"),
    url(r'^delete/(?P<id>\d+)', 'core.views.delete_comic', name="delete_comic"),
    #-----------------------

    #-------- query --------
    url(r'^search/$', 'core.query.search', name="search"),
    #-----------------------
)