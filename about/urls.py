from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.about_views),
    url(r'^author/$',views.aboutme_views)
]