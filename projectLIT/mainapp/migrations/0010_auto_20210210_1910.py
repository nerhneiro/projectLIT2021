# Generated by Django 2.2 on 2021-02-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210208_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='tags',
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_albums', to='mainapp.Tag'),
        ),
    ]
