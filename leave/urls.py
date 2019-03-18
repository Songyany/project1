from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^leave/$', views.gbook_views),
]