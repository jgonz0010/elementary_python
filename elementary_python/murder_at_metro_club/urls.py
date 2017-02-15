from django.conf.urls import url
from murder_at_metro_club import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
