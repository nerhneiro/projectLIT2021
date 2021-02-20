# Generated by Django 2.2 on 2021-02-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_siteuser_albums'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='yandexEmail',
            field=models.EmailField(blank=True, max_length=128, verbose_name='Yandex email'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='yandexPassword',
            field=models.CharField(blank=True, max_length=256, verbose_name='Yandex password'),
        ),
    ]