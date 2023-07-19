from django.urls import path

from .views import clientes, ordem_de_servico_view

urlpatterns = [
    path('clientes/', clientes, name='clientes'),
    path('ordem_de_servico/', ordem_de_servico_view),
]
