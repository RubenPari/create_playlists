from django.urls import path

from . import views

urlpatterns = [
    path('hip-pop', views.hip_pop, name='hip_pop'),
    path('rock', views.rock, name='rock'),
    path('edm', views.edm, name='edm'),
    path('pop', views.pop, name='pop'),
]
