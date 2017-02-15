from django.conf.urls import url
from clergyman_peter import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
