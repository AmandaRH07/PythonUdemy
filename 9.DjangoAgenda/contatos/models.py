"""CONTATOS
id: INT (automático)
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

CATEGORIA
id: INT
nome: STR * (obrigatório)
"""

from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Contato(models.Model):
    # campo de texto com no máximo 255 caracteres
    nome = models.CharField(max_length=255)
    # blank = não obrigatório
    sobrenome = models.CharField(max_length=255, blank= True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    # relação entre tabelas
    # on_delete = se a categoria for apagada, não acontece nada
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

# agora precisa fazer as migrações: python manage.py makemigrations
