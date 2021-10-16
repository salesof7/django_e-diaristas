from django.shortcuts import render, redirect
from .forms import diarista_form
from .models import Diarista

def cadastrar_diarista(request):
    """Função que cadastra o(a) diarista no banco de dados através do formulário"""

    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm()

    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})


def listar_diaristas(request):
    """Lista todas os(as) diaristas que estão no banco de dados"""
    
    diaristas = Diarista.objects.all()
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})


def editar_diarista(request, diarista_id):
    """Edita os dados de um(a) diarista do banco de dados através do id"""

    diarista = Diarista.objects.get(id = diarista_id)
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST or None, request.FILES, instance=diarista)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm(instance=diarista)
    
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})


def remover_diarista(request, diarista_id):
    """Remove os dados de um(a) diarista do banco de dados através do id"""
    diarista = Diarista.objects.get(id = diarista_id)
    diarista.delete()
    return redirect('listar_diaristas')
