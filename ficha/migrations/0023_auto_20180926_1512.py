# Generated by Django 2.0.7 on 2018-09-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0022_auto_20180926_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='fc',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='fr',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pad',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pas',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
