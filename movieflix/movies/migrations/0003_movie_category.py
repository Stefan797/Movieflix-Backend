# Generated by Django 4.1.4 on 2023-06-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_video_file_movie_movie_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
