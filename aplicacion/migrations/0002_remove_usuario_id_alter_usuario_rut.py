# Generated by Django 4.2.2 on 2023-06-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]