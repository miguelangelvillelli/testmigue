# Generated by Django 3.2.6 on 2021-08-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dependencia', '0003_auto_20210818_0816'),
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='last_name',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='dependency',
        ),
        migrations.AddField(
            model_name='empleado',
            name='dependencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dependencia.dependencia', verbose_name='Dependencia'),
            preserve_default=False,
        ),
    ]
