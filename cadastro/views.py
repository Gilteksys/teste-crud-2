from django.shortcuts import render, redirect
from .forms import ClienteForm, OrdemDeServicoForm
from .models import OrdemDeServico


def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes.html', {'form': form})


def ordem_servico(request):
    if request.method == 'POST':
        form = OrdemDeServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalhes')
    else:
        form = OrdemDeServicoForm()
    return render(request, 'ordem_servico.html', {'form': form})




    

