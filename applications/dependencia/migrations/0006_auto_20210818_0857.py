# Generated by Django 3.2.6 on 2021-08-18 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependencia', '0005_auto_20210818_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sede',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='sede',
            name='piso',
        ),
    ]