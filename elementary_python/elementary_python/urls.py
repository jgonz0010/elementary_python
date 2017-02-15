"""elementary_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from elementary_python import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^murder_at_metro_club/', include('murder_at_metro_club.urls')),
    url(r'^holmes_gives_a_demo/', include('holmes_gives_a_demo.urls')),
    url(r'^bathing_machine/', include('bathing_machine.urls')),
    url(r'^cigar_ash/', include('cigar_ash.urls')),
    url(r'^clergyman_peter/', include('clergyman_peter.urls')),
    url(r'^holmes_method_revealed/', include('holmes_method_revealed.urls')),
    url(r'^advertisement_in_times/', include('advertisement_in_times.urls')),
    url(r'^ciphered_message/', include('ciphered_message.urls')),
    url(r'^study_in_chemistry/', include('study_in_chemistry.urls')),
    url(r'^coroner_report/', include('coroner_report.urls')),
    url(r'^gold_chip/', include('gold_chip.urls')),
    url(r'^holmes_delivers_a_lecture/', include('holmes_delivers_a_lecture.urls')),
    url(r'^final_programme/', include('final_programme.urls')),
    url(r'^admin/', admin.site.urls),
]
