

from django.contrib.auth.models import User
from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Skill(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class UsuarioSkill(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    nivel = models.IntegerField()  # Exemplo: 1 a 5 para o nível de skill

class Permissao(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pode_editar = models.BooleanField(default=False)

