# Generated by Django 3.2.6 on 2021-08-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependencia', '0008_auto_20210818_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencia',
            name='lado',
            field=models.CharField(blank=True, choices=[('0', 'Frente'), ('1', 'Contrafrente')], max_length=1, verbose_name='Lado'),
        ),
        migrations.AlterField(
            model_name='dependencia',
            name='oficina',
            field=models.CharField(blank=True, max_length=50, verbose_name='Oficina'),
        ),
    ]