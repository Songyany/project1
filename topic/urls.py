from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^topic/$',views.list_views),
    url(r'^taglist/$',views.taglist_views),
]