# Generated by Django 4.1.4 on 2023-07-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='moviename',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
