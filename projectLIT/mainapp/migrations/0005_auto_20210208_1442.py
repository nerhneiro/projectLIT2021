# Generated by Django 2.2 on 2021-02-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_album_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='labels',
            field=models.ManyToManyField(to='mainapp.Label'),
        ),
    ]
