# Generated by Django 2.2 on 2021-02-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210223_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='country',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
