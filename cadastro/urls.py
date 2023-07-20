from django.urls import path
from .views import clientes, ordem_servico

urlpatterns = [
    path('clientes/', clientes, name='clientes'),
    path('ordem_servico/', ordem_servico, name='ordem_servico'),
]
