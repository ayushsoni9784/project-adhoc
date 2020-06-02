from django.urls import path 
from dockerimage_app import views

urlpatterns = [
    path('', views.services, name='services'),
    path('build-image', views.buildimage, name='buildimage'),

]
