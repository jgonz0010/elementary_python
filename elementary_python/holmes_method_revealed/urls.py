from django.conf.urls import url
from holmes_method_revealed import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
