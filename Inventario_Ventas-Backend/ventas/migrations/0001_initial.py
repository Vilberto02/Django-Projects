# Generated by Django 4.2.6 on 2024-08-10 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500, verbose_name='Nombre')),
                ('dni', models.PositiveIntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400, verbose_name='Nombre')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, verbose_name='Nombre')),
                ('telefono', models.PositiveIntegerField(verbose_name='Telefono')),
                ('ruc', models.PositiveIntegerField(verbose_name='RUC')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descuento', models.FloatField(verbose_name='Descuento')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Venta_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto', verbose_name='ID Producto')),
                ('venta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta', verbose_name='ID Venta')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.proveedor'),
        ),
        migrations.CreateModel(
            name='Cliente_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente', verbose_name='ID Cliente')),
                ('venta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta', verbose_name='ID Venta')),
            ],
        ),
    ]
