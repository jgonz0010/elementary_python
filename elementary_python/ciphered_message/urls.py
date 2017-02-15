from django.conf.urls import url
from ciphered_message import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
