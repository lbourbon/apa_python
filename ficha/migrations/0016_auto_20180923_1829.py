# Generated by Django 2.0.7 on 2018-09-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0015_auto_20180923_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='exfisico',
            field=models.TextField(blank=True, default='Geral: B.E.G., L.O.T.E., eupnéico, normocorado, hidratado \n    ACV: Bulhas rítmicas, normofonéticas, em dois tempos, sem sopros \n    AR: Múrmurios vesiculares presentes bilateralmente, sem ruídos adventícios \n\\ ', max_length=500),
        ),
    ]