# Generated by Django 3.2.9 on 2021-11-15 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario de modificación')),
                ('descripcion', models.CharField(help_text='Descripción de la categoría', max_length=100, verbose_name='Descripción')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario de modificación')),
                ('descripcion', models.CharField(help_text='Descripción de la marca', max_length=100, verbose_name='Descripción')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario de modificación')),
                ('descripcion', models.CharField(help_text='Descripción de la subcategoría', max_length=100, verbose_name='Descripción')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SubCategorías',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario de modificación')),
                ('descripcion', models.CharField(help_text='Descripción del producto', max_length=100, verbose_name='Descripcion')),
                ('stock', models.IntegerField(default=0)),
                ('preciodistrib', models.IntegerField(default=0)),
                ('precioferret', models.IntegerField(default=0)),
                ('preciopubl', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.marca')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.subcategoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]