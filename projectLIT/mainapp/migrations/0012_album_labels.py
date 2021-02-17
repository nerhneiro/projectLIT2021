# Generated by Django 2.2 on 2021-02-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_album_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='labels',
            field=models.ManyToManyField(related_name='labeled_albums', to='mainapp.Tag'),
        ),
    ]