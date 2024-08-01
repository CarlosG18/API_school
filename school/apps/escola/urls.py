from django.urls import path
from . import views

urlpatterns = [
    path('', views.estudantes, name="estudantes"),
]