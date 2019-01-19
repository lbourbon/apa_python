from django.db import models
from .choices import *
from customauth.models import MyUser


class Ficha(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    nome = models.CharField(max_length=100, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    sexo = models.CharField(choices=SEXO_CHOICES, blank=True, max_length=10, default="0")
    cpf = models.CharField(max_length=30, blank=True)
    hosp = models.CharField(max_length=50, blank=True)
    convenio = models.CharField(max_length=30, blank=True)
    cirurgia = models.CharField(max_length=100, blank=True)
    cirurgiao = models.CharField(max_length=50, blank=True)

    peso = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
    altura = models.DecimalField(decimal_places=0, max_digits=5, null=True, blank=True)
    imc = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
    ideal = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
    ajustado = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
    predito = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)

    bool_previo = models.BooleanField(default=False)
    c_previa = models.CharField(max_length=100, blank=True)
    a_previa = models.CharField(max_length=100, blank=True)
    bool_adverso = models.BooleanField(default=False)
    e_adversos = models.CharField(max_length=100, blank=True)
    bool_alergias = models.BooleanField(default=False)
    alergias = models.CharField(max_length=200, blank=True, default="")

    bool_doencas = models.BooleanField(default=False)
    mets = models.CharField(choices=METS_CHOICES, blank=True, max_length=20, default="1")
    cardio_has = models.BooleanField(default=False)
    cardio_arr = models.BooleanField(default=False)
    cardio_cor = models.BooleanField(default=False)
    cardio_icc = models.BooleanField(default=False)
    cardio_out = models.BooleanField(default=False)
    neuro_avc = models.BooleanField(default=False)
    neuro_cef = models.BooleanField(default=False)
    neuro_con = models.BooleanField(default=False)
    neuro_lme = models.BooleanField(default=False)
    neuro_out = models.BooleanField(default=False)
    resp_asm = models.BooleanField(default=False)
    resp_apn = models.BooleanField(default=False)
    resp_dpo = models.BooleanField(default=False)
    resp_tbg = models.BooleanField(default=False)
    resp_iva = models.BooleanField(default=False)
    resp_out = models.BooleanField(default=False)
    gastro_rge = models.BooleanField(default=False)
    gastro_gas = models.BooleanField(default=False)
    gastro_vom = models.BooleanField(default=False)
    gastro_obs = models.BooleanField(default=False)
    gastro_out = models.BooleanField(default=False)
    endocrino_dia = models.BooleanField(default=False)
    endocrino_dti = models.BooleanField(default=False)
    endocrino_dlp = models.BooleanField(default=False)
    endocrino_out = models.BooleanField(default=False)
    renal_irc = models.BooleanField(default=False)
    renal_ira = models.BooleanField(default=False)
    renal_dia = models.BooleanField(default=False)
    renal_out = models.BooleanField(default=False)
    hem_coa = models.BooleanField(default=False)
    hem_ane = models.BooleanField(default=False)
    hem_tra = models.BooleanField(default=False)
    hem_hep = models.BooleanField(default=False)
    hem_hiv = models.BooleanField(default=False)
    hem_out = models.BooleanField(default=False)
    musc_lom = models.BooleanField(default=False)
    musc_des = models.BooleanField(default=False)
    musc_ati = models.BooleanField(default=False)
    musc_ato = models.BooleanField(default=False)
    musc_dis = models.BooleanField(default=False)
    musc_out = models.BooleanField(default=False)

    bool_med = models.BooleanField(default=False)
    medicacoes = models.TextField(max_length=500, blank=True)
    bool_exfisico = models.BooleanField(default=False)
    exfisico = models.TextField(max_length=500, blank=True, default=default['físico'])
    pas = models.IntegerField(default=0, null=True, blank=True)
    pad = models.IntegerField(default=0, null=True, blank=True)
    fc = models.IntegerField(default=0, null=True, blank=True)
    fr = models.IntegerField(default=0, null=True, blank=True)
    temp = models.CharField(max_length=10, blank=True, default=default['temp'])

    mallampati = models.CharField(choices=mallampati_CHOICES, blank=True, max_length=20)
    distem = models.CharField(choices=distem_CHOICES, blank=True, max_length=20)
    mobcer = models.CharField(choices=mobcer_CHOICES, blank=True, max_length=20)
    aboral = models.CharField(choices=aboral_CHOICES, blank=True, max_length=20)
    protese = models.CharField(choices=protese_CHOICES, blank=True, max_length=20)
    vad = models.CharField(choices=vad_CHOICES, blank=True, max_length=20)

    hb = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    ht = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    leuco = models.DecimalField(decimal_places=0, max_digits=8, null=True, blank=True)
    plt = models.DecimalField(decimal_places=0, max_digits=8, null=True, blank=True)
    gli = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    u = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    cr = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    na = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    k = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    ts = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    tc = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    inr = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    tp = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    ttpa = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    tgo = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    tgp = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    fa = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    ggt = models.DecimalField(decimal_places=1, max_digits=8, null=True, blank=True)
    outros_lab = models.CharField(max_length=200, blank=True)

    ecg = models.CharField(max_length=200, blank=True)
    eco = models.CharField(max_length=200, blank=True)
    rx = models.CharField(max_length=200, blank=True)
    ergo = models.CharField(max_length=200, blank=True)
    outroex = models.TextField(max_length=500, blank=True)
    anotacoes = models.TextField(max_length=500, blank=True)
    anotacoes2 = models.CharField(max_length=200, blank=True)
    proposta = models.CharField(max_length=200, blank=True)
    jejum = models.CharField(max_length=200, blank=True)
    prescricao = models.CharField(max_length=200, blank=True)
    prescricao2 = models.CharField(max_length=200, blank=True)
    prescricao3 = models.CharField(max_length=200, blank=True)
    asa = models.PositiveSmallIntegerField(default=1, blank=True)

    def __str__(self):
        return self.nome
