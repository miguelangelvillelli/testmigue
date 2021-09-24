# Generated by Django 3.2.6 on 2021-08-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependencia', '0007_remove_sede_sigla'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependencia',
            name='oficina',
            field=models.CharField(default=1, max_length=50, verbose_name='Oficina'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dependencia',
            name='lado',
            field=models.CharField(choices=[('0', 'Frente'), ('1', 'Contrafrente')], max_length=1, null=True, verbose_name='Lado'),
        ),
    ]