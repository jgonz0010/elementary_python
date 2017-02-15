from django.conf.urls import url
from advertisement_in_times import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
