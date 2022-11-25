# Generated by Django 4.1.2 on 2022-11-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0004_rename_precio_persona_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]