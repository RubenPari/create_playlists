from django.urls import path

from . import views

urlpatterns = [
    path('/hip-hop', views.hip_hop, name='hip_hop'),
    path('/rock', views.rock, name='rock'),
    path('/edm', views.edm, name='edm'),
    path('/pop', views.pop, name='pop'),
]
