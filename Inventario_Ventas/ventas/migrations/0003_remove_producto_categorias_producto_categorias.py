# Generated by Django 4.2.5 on 2023-09-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_rename_productos_categoria_productos_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categorias',
        ),
        migrations.AddField(
            model_name='producto',
            name='categorias',
            field=models.ManyToManyField(to='ventas.categoria'),
        ),
    ]
