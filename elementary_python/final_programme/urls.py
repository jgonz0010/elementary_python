from django.conf.urls import url
from final_programme import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
