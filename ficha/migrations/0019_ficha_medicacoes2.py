# Generated by Django 2.0.5 on 2018-06-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0018_auto_20180602_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='medicacoes2',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]