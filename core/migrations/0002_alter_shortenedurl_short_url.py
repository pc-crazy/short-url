# Generated by Django 3.2.12 on 2022-03-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_url',
            field=models.URLField(unique=True),
        ),
    ]
