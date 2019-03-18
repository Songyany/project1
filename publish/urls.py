from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^publish/$', views.release_views),
    url(r'^info/$', views.info_views),
    url(r'^pag_info/$', views.pag_info_views)
]