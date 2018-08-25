from django.db import models
from django.contrib.auth.models import User

class Fichateste(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


    '''
   width:auto;
    height:auto;
    max-height:91.4vh;

    '''