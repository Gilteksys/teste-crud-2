from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import OrdemDeServico

def ordem_de_servico_view(request):
    ordem_de_servico = OrdemDeServico.objects.all()
    return render(request, 'ordem_de_servico.html', {'ordem_de_servico': ordem_de_servico})


def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes.html', {'form': form})

