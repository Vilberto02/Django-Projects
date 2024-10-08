# Generated by Django 4.2.6 on 2023-10-17 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Edad')),
                ('is_activate', models.BooleanField(default=True, verbose_name='¿Esta activo?')),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Nombres')),
                ('nickname', models.CharField(max_length=50, verbose_name='Username')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Edad')),
                ('is_activate', models.BooleanField(default=True, verbose_name='¿Esta activo?')),
            ],
        ),
    ]
