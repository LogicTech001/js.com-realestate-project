
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('accodition', views.accodition, name='accodition'),
    path('contact', views.contact, name='contact'),
    path('furniture', views.furniture, name='furniture'),
    path('maintenance', views.maintenance, name='maintenance'),
    path('painting', views.painting, name='painting'),
    path('plumbing', views.plumbing, name='plumbing'),
    path('tilesfix', views.tilesfix, name='tilesfix'),
    path('electrical', views.electrical, name='electrical'),
    path('ourservices1', views.ourservices1, name='ourservices1'),
    path('ourservices2', views.ourservices2, name='ourservices2'),
    
]
