# Generated by Django 5.0.4 on 2024-05-04 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dronename', models.IntegerField(verbose_name='Drone')),
                ('location', models.CharField(max_length=30)),
                ('battiere', models.IntegerField(verbose_name='Battiere Percent')),
                ('active', models.BooleanField(verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('displayname', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('access', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertname', models.CharField(max_length=30, verbose_name='Alert')),
                ('alertdescription', models.TextField(verbose_name='Description')),
                ('dronetarget', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logins_and_alerts.drones')),
            ],
        ),
    ]
