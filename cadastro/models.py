from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField()

class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateTimeField()
    status = models.CharField(max_length=255)

