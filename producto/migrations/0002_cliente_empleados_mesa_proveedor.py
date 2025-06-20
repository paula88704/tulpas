# Generated by Django 5.2.1 on 2025-06-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mesa', models.CharField(max_length=10, unique=True)),
                ('capacidad', models.IntegerField(default=2)),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('ocupada', 'Ocupada'), ('reservada', 'Reservada')], default='disponible', max_length=10)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Mesas',
                'ordering': ['numero_mesa'],
            },
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-nombre'],
            },
        ),
    ]
