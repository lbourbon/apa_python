# Generated by Django 2.0.5 on 2018-08-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0031_auto_20180623_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='dn',
        ),
        migrations.AddField(
            model_name='ficha',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]