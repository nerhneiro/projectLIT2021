# Generated by Django 2.2 on 2021-02-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210223_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]