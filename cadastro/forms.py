from django.forms import ModelForm

from .models import Cliente, OrdemDeServico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class OrdemDeServicoForm(ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = '__all__'
