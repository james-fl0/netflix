# Generated by Django 4.1.7 on 2023-11-05 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_movie_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='id',
            new_name='uid',
        ),
    ]
