# Generated by Django 4.0.4 on 2022-05-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('comunicacion', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Smartmeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Webclient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
