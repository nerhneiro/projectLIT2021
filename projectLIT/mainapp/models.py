from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name="Tag's name", max_length=128)

class Artist(models.Model):
    idDiscogs =  models.PositiveIntegerField(verbose_name="DiscogsID артиста")
    name = models.CharField(verbose_name="Artist's name", max_length=128)

class Label(models.Model):
    name = models.CharField(verbose_name="Label's name", max_length=128)
    idDiscogs = models.PositiveIntegerField(verbose_name="DiscogsID")
    #albums = models.ManyToManyField(Album)

class Album(models.Model):
    idYandex = models.PositiveIntegerField(verbose_name="YandexMusicID")
    idDiscogs = models.PositiveIntegerField(verbose_name="DiscogsID")
    idDiscogsSecondary = models.PositiveIntegerField(verbose_name="DiscogsSecondaryID")
    name = models.CharField(verbose_name="Album's name", max_length=128)
    image = models.ImageField(upload_to='Cover image', blank=True)
    artist = models.ForeignKey(Artist, verbose_name="Artist", null=True, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, null=True)
    labels = models.ManyToManyField(Label, blank=True)
#     #image field
#     #from spotify/yandex check

