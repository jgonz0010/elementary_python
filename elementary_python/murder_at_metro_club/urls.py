from django.conf.urls import url
from murder_at_metro_club import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<suspect_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^(?P<suspect_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^edit/$', views.edit, name='edit'),
]
