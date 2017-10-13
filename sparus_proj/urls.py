"""sparus_proj URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
#icq
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#icq
    url(r'pmet/$', views.pmet),
#icq
    url(r'pmet/day$', views.day),
#icq
    url(r'pmet/week$', views.week),
#icq
    url(r'pmet/month$', views.month),
#icq
    url(r'pmet/xls$', views.xls),
#exports
    url(r'^pmet/em_csv$', views.em_csv, name='embalse_csv'),
    url(r'^pmet/es_csv$', views.es_csv, name='estanque_csv'),
    url(r'^pmet/eto_csv$', views.eto_csv, name='eto_csv'),

    url(r'^pmet/em7_csv$', views.em7_csv, name='embalse7_csv'),
    url(r'^pmet/es7_csv$', views.es7_csv, name='estanque7_csv'),
    url(r'^pmet/eto7_csv$', views.eto7_csv, name='eto7_csv'),

    url(r'^pmet/em30_csv$', views.em30_csv, name='embalse30_csv'),
    url(r'^pmet/es30_csv$', views.es30_csv, name='estanque30_csv'),
    url(r'^pmet/eto30_csv$', views.eto30_csv, name='eto30_csv'),

    url(r'^pmet/em90_csv$', views.em90_csv, name='embalse90_csv'),
    url(r'^pmet/es90_csv$', views.es90_csv, name='estanque90_csv'),
    url(r'^pmet/eto90_csv$', views.eto90_csv, name='eto90_csv'),
]
