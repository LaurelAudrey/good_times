from django.urls import path
from gtapp import views

urlpatterns = [
    path('', views.hello_gt, name='hello_gt'),
]