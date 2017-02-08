#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2016-11-23 20:43:37
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2016-11-23 20:43:50

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]