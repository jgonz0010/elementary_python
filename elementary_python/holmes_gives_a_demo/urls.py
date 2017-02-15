from django.conf.urls import url
from holmes_gives_a_demo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
