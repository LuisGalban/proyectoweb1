# Generated by Django 3.1.8 on 2021-06-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_nombre_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='psinopsis',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='nombre_genero',
        ),
    ]
