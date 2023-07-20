from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    aparelho = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=25)
    descricao = models.TextField()

    def __str__(self):
        return self.aparelho
