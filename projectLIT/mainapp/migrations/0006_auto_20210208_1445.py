# Generated by Django 2.2 on 2021-02-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210208_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='labels',
            field=models.ManyToManyField(blank=True, to='mainapp.Label'),
        ),
    ]