from django.conf.urls import url
from cigar_ash import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
