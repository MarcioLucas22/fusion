# Generated by Django 5.0.6 on 2024-07-02 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_funcionalidade_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionalidade',
            options={'verbose_name': 'Funcionalidade', 'verbose_name_plural': 'Funcionalidades'},
        ),
    ]
