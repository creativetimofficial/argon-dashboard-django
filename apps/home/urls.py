# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from django.views.generic import RedirectView
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Cell visualization page
    path('cells/', views.cells, name='cells'),

    # Cameron's research page
    path('cameron-research/', views.cameron_research, name='cameron_research'),

    # People pages
    path('people/', views.people, name='people'),
    path('people.html', RedirectView.as_view(url='/people/', permanent=False)),
    path('profile/<str:username>/', views.profile, name='profile'),

    # Ideas page redirect
    path('ideas.html', views.pages, name='ideas'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
