# Generated by Django 4.1.4 on 2023-07-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_moviename_movie_search_terms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category_german',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
