from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_views),
    url(r'^register/$', views.register_views),
    url(r'^loginout/$', views.loginout_views),
]