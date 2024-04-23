from django.urls import path,include
from recommendermodel import views

urlpatterns = [
    path('', views.home, name='home'),
]
