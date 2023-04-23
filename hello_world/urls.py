# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^helloworld/$', views.helloworld),
]

# urlpatterns = (
#     # url(r'^$', views.home),
#     # url(r'^dev-guide/$', views.dev_guide),
#     # url(r'^contact/$', views.contact),
#     # # 添加 helloworld 路由
#     url(r'^helloworld/$', views.helloworld),
# )