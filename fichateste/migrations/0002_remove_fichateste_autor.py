# Generated by Django 2.0.7 on 2018-08-22 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichateste', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichateste',
            name='autor',
        ),
    ]