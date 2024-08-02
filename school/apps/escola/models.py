from django.db import models

class Estudantes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=False)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField()
    telefone = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.nome

class Curso(models.Model):
    NIVEL_CHOICES = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )

    codigo = models.CharField(max_length=10)
    descricao = models.TextField()
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES,blank=False, null=False, default='B')

    def __str__(self) -> str:
        return self.codigo