# Generated by Django 4.0.4 on 2022-06-04 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_newsheading_remove_news_newsheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='newsheading',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.newsheading'),
        ),
    ]