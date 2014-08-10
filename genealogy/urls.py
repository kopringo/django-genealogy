#-*- coding: utf-8 -*-

#django
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('genealogy',
                       
                       
    # strona glowna
    
    
    
    url(r'^person-list$',                      'views.person_list',  name='person_list'),
    url(r'^person-view/(?P<handle>.*)/$',      'views.person_view',  name='person_view'),
    
    url(r'^family-list$',                      'views.family_list',  name='family_list'),
    
    url(r'^branch-list$',                       'views.branch_list', name='branch_list'),
    
    url(r'^test$',                              'views.test'),
    
    # mechanizm przelaczania wersji jezykowej
    #url(r'^lang/(?P<id>[plen]+)',   'views.lang',   name='lang'),
    
    url(r'^$', 'views.home', name='home'),
)
