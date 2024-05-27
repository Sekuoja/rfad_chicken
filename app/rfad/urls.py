from django.urls import path

from rfad import views

urlpatterns = [
    path('', views.index, name='home')
]
