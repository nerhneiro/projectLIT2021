# Generated by Django 2.2 on 2021-02-12 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210210_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='labels',
        ),
    ]