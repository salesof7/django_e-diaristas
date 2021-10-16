from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_diarista', views.cadastrar_diarista, name='cadastrar_diarista'),
    path('listar_diaristas', views.listar_diaristas, name='listar_diaristas'),
    path('editar_diarista/<int:diarista_id>', views.editar_diarista, name='editar_diarista'),
    path('remover_diarista/<int:diarista_id>', views.remover_diarista, name='remover_diarista'),
]