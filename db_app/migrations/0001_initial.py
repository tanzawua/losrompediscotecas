# Generated by Django 4.1.2 on 2022-11-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('cedula', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('estado', models.BooleanField(default=True)),
                ('valor', models.IntegerField(default=0)),
                ('valor1', models.IntegerField(default=0)),
            ],
        ),
    ]
