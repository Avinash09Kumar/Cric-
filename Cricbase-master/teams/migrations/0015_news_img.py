# Generated by Django 4.0.4 on 2022-06-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0014_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Img',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
    ]
