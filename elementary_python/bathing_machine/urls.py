from django.conf.urls import url
from bathing_machine import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
