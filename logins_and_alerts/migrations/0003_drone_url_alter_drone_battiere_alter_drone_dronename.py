# Generated by Django 5.0.4 on 2024-05-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins_and_alerts', '0002_user_rename_alerts_alert_rename_drones_drone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='drone',
            name='battiere',
            field=models.CharField(max_length=3, verbose_name='Battiere Percent'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='dronename',
            field=models.CharField(max_length=7, verbose_name='Drone'),
        ),
    ]
