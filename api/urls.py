from django.urls import path
from . import views

urlpatterns = [
    path('diaristas-cidade', views.DiaristasCidadeList.as_view(), name='diaristas-cidade-list'),
]