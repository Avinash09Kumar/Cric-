# Generated by Django 4.0.4 on 2022-06-05 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0025_venue_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.user'),
        ),
    ]
