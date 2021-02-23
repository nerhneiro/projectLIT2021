# Generated by Django 2.2 on 2021-02-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_album_labels'),
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='albums',
            field=models.ManyToManyField(blank=True, to='mainapp.Album', verbose_name='albums'),
        ),
    ]