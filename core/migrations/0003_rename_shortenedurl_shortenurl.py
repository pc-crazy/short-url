# Generated by Django 3.2.12 on 2022-03-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_shortenedurl_short_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShortenedUrl',
            new_name='ShortenUrl',
        ),
    ]
