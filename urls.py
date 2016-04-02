from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/about/', views.about, name='about'),
    url(r'^/becomesponsor/', views.becomesponsor, name='becomesponsorsponsor'),
    url(r'^/blog/', views.blog, name='blog'),
    url(r'^/callforpapers/', views.papers, name='papers'),
    url(r'^/policies/', views.policies, name='policies'),
    url(r'^/schedule/', views.schedule, name='schedule'),
    url(r'^/social/', views.social, name='social'),
    url(r'^/sponsors/$', views.sponsors, name='sponsors'),
    url(r'^/sponsors/becomesponsor/', views.becomesponsor, name='becomesponsor'),
    url(r'^/tickets/', views.tickets, name='tickets'),
    url(r'^/venue/', views.venue, name='venue'),
]