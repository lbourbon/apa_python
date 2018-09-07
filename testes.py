class FichaForm():
    class Meta:
        model = 'Ficha'
        fields = [
            'data', 'nome', 'idade', 'sexo', 'cpf', 'hosp', 'convenio', 'cirurgia', 'cirurgiao', 'peso', 'altura', 'imc',
            'n_previa', 'c_previa', 'a_previa', 'n_adversos', 'adversos', 'mets', 'cardio_neg', 'cardio_has', 'cardio_arr',
            'cardio_cor', 'cardio_icc', 'cardio_out', 'neuro_neg', 'neuro_avc', 'neuro_cef', 'neuro_con', 'neuro_lme',
            'neuro_out', 'resp_neg', 'resp_asm', 'resp_dpo','resp_tbg', 'resp_iva', 'resp_out', 'gastro_neg', 'gastro_rge',
            'gastro_gas', 'gastro_vom', 'gastro_obs', 'gastro_out', 'endocrino_neg', 'endocrino_dia', 'endocrino_dti',
            'endocrino_dlp', 'endocrino_out', 'renal_neg', 'renal_irc', 'renal_ira', 'renal_dia', 'renal_out', 'hem_neg',
            'hem_coa', 'hem_ane', 'hem_tra', 'hem_hep', 'hem_hiv', 'hem_out', 'musc_neg', 'musc_lom', 'musc_des', 'musc_ati',
            'musc_ato', 'musc_dis', 'musc_out','medicacoes', 'medicacoes2', 'alergias', 'geral', 'acv', 'ar', 'abd', 'ext',
            'pas', 'pad', 'fc', 'fr', 'temp', 'mallampati', 'distem', 'mobcer', 'aboral', 'protese', 'vad', 'hb', 'ht',
            'leuco', 'plt', 'gli', 'u', 'cr', 'na', 'k', 'ts', 'tc', 'inr', 'tp', 'ttpa', 'ecg', 'eco', 'rx', 'ergo',
            'outroex', 'anotacoes', 'anotacoes2', 'proposta', 'jejum', 'prescricao', 'prescricao2', 'prescricao3', 'asa',
        ]
        exclude = ['user', ]

for i in (FichaForm.Meta.fields):
    print(i)