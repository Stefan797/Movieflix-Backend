# Generated by Django 4.1.4 on 2023-08-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_movie_movie_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('keepwatching', 'keepwatching'), ('popularatpresent', 'popularatpresent'), ('watchagain', 'watchagain'), ('mylist', 'mylist'), ('any', 'any'), ('nature', 'nature'), ('vehicles', 'vehicles'), ('funny', 'funny'), ('animals', 'animals'), ('programming', 'programming'), ('sea', 'sea')], default='any', max_length=50),
        ),
    ]
