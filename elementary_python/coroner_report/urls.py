from django.conf.urls import url
from coroner_report import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
