# Generated by Django 4.2.1 on 2023-06-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='idCard',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
