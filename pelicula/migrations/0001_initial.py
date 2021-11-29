# Generated by Django 3.2.7 on 2021-10-02 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Actuacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelicula.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
                ('actores', models.ManyToManyField(through='pelicula.Actuacion', to='pelicula.Actor')),
            ],
        ),
        migrations.AddField(
            model_name='actuacion',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelicula.pelicula'),
        ),
    ]
