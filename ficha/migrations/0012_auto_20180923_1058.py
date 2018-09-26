# Generated by Django 2.0.7 on 2018-09-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0011_auto_20180923_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='medicacoes2',
        ),
        migrations.AddField(
            model_name='ficha',
            name='bool_med',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='medicacoes',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
