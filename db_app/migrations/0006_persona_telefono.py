# Generated by Django 4.1.2 on 2022-11-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0005_persona_email_alter_persona_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
