from django.urls import path

from . import views

urlpatterns = [
    path('reporte', views.index, name='index'),
]
