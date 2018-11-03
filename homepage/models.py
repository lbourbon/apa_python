from django.db import models


class Espera(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email', max_length=255)
    fone = models.CharField(max_length=19)

    def __str__(self):
        return str(self.nome)