# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from statistical_computing_interface.sciApp import views

urlpatterns = patterns('statistical_computing_interface.sciApp.views',
    url(r'^upload/$', 'list', name='list'),
    url(r'^plot_bar/$', 'makeBarGraph', name='makeBarGraph'),
    url(r'^plot_line/$', 'makeLineGraph', name='makeLineGraph'),
    url(r'^login/$','login',name='login'),
    url(r'^choose_graph/$','chooseGraph',name='chooseGraph'),
    url(r'^register/$','register',name='register'),
    url(r'^register_status/$','registerStatus',name='registerStatus'),
    url(r'^login_status/$','loginStatus',name='loginStatus'),
    url(r'^openCPU_output/$','OpenCPUAnalysis',name='OpenCPUAnalysis'),
    #url(r'^plot/$', 'plot', name='plot'),
)
