# Generated by Django 4.0.3 on 2022-06-05 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0031_teams_players_playerinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playerinfo',
            options={'verbose_name_plural': 'Playerinfo'},
        ),
        migrations.AlterModelOptions(
            name='players',
            options={'verbose_name_plural': 'Players'},
        ),
        migrations.AlterModelOptions(
            name='teams',
            options={'verbose_name_plural': 'Teams'},
        ),
        migrations.RemoveField(
            model_name='playerinfo',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='players',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='teams',
        ),
    ]
