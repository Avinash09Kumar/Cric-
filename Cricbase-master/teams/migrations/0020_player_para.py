# Generated by Django 4.0.4 on 2022-06-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0019_player_cen_player_cts_player_hcen_player_hs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='para',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Para'),
        ),
    ]