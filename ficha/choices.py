default = {
    'temp':'AFEBRIL',
    'alergias':'DESCONHECE ALERGIAS',
    'geral': 'BEG, L.O.T.E., EUPNEICO, NORMOCORADO, HIDRATADO',
    'acv': 'BULHAS RÍTMICAS, NORMOFONÉTICAS, EM DOIS TEMPOS, SEM SOPROS',
    'ar': 'MURMÚRIOS VESICULARES PRESENTES BILATERALMENTE, SEM RUÍDOS ADVENTÍCIOS',
    'abd': 'N.D.N.',
    'ext': 'N.D.N.',
    '': '',
}
SEXO_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Masculino'),
    ('2', 'Feminino'),
    ('9', 'Não se aplica')
)
METS_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Maior que 4 mets'),
    ('2', 'Menor que 4 mets'),
    ('9', 'Impossível Avaliar'),
)

mallampati_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
)
distem_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Maior que 12cm'),
    ('2', 'Menor que 12cm')
)
mobcer_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Boa'),
    ('2', 'Limitada')
)
aboral_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Maior que 4cm'),
    ('2', 'Menor que 4cm')
)
protese_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Não'),
    ('2', 'Sim')
)
vad_CHOICES = (
    ('0', 'Desconhecido'),
    ('1', 'Não'),
    ('2', 'Sim')
)