# Generated by Django 2.0.5 on 2018-06-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0017_auto_20180601_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='abd',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ficha',
            name='acv',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ficha',
            name='alergias',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ficha',
            name='ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ficha',
            name='ext',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ficha',
            name='fc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ficha',
            name='fr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ficha',
            name='geral',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ficha',
            name='medicacoes',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='ficha',
            name='pad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ficha',
            name='pas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ficha',
            name='temp',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='endocrino_neg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='gastro_neg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='hem_neg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='musc_neg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='neuro_neg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='renal_neg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='resp_neg',
            field=models.BooleanField(default=True),
        ),
    ]
