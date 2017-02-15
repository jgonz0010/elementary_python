from django.conf.urls import url
from gold_chip import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
