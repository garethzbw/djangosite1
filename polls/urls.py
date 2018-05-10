#!/usr/bin/env python
# coding=utf-8

from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('answer', views.answer, name='answer'),
    path('results', views.results, name='results'),
]