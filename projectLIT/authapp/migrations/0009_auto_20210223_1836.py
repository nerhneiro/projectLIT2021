# Generated by Django 2.2 on 2021-02-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210223_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='emailYM',
            field=models.EmailField(blank=True, max_length=128, verbose_name='yandex Music email'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='passwordYM',
            field=models.CharField(blank=True, max_length=256, verbose_name='Yandex Music password'),
        ),
    ]
