# Generated by Django 5.2.3 on 2025-06-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0005_alter_song_artist_alter_song_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="artist",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="song",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
