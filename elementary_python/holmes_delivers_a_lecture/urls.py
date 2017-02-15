from django.conf.urls import url
from holmes_delivers_a_lecture import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
