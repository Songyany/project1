from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',views.index),
    url(r'^index/$',views.index),
    # url(r'^search$',views.search_views)
    # url(r'^login/$',views.login_views),
    # url(r'^register/$',views.register_views),
    # url(r'^loginout/$',views.loginout_views),
    # url(r'^recommend/$',views.recommend_views),
    # url(r'^photo/$', views.photo_views),
    # url(r'^time/$', views.time_views),
    # url(r'^gbook/$', views.gbook_views),
    # url(r'^about/$', views.about_views),
    # url(r'^release/$', views.release_views),
    # url(r'^list/$',views.list_views),
    # url(r'^info/',views.info_views),
    # url(r'^pag_info/',views.pag_info_views)
]