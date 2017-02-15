from django.conf.urls import url
from study_in_chemistry import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
