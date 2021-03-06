from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name="Tag's name", max_length=128)

class Artist(models.Model):
    idDiscogs = models.PositiveIntegerField(verbose_name="DiscogsID артиста")
    name = models.CharField(verbose_name="Artist's name", max_length=128)

class Label(models.Model):
    name = models.CharField(verbose_name="Label's name", max_length=128)
    idDiscogs = models.PositiveIntegerField(verbose_name="DiscogsID")
    #albums = models.ManyToManyField(Album)

class Genre(models.Model):
    name = models.CharField(verbose_name='genre', max_length=128)

class Style(models.Model):
    name = models.CharField(verbose_name='style', max_length=128)

class Album(models.Model):
    idYandex = models.PositiveIntegerField(verbose_name="YandexMusicID")
    idDiscogs = models.PositiveIntegerField(verbose_name="DiscogsID")
    idDiscogsSecondary = models.PositiveIntegerField(verbose_name="DiscogsSecondaryID", null=True)
    name = models.CharField(verbose_name="Album's name", max_length=128)
    imageURL = models.CharField(verbose_name='Image url', max_length=512, default='', null=True)
    artists = models.ManyToManyField(Artist, verbose_name="Artists", blank=True, related_name='albums')
    #tags = models.ManyToManyField(Tag, blank=True)
    #tags = models.ForeignKey(Tag, verbose_name="Tags", null=True, on_delete=models.CASCADE)
    #labels = models.ManyToManyField(Label, blank=True)
    #labelsChoices = Label.objects.all()
    # labelsChoices = []
    # for i in Label.objects.all():
    #     labelsChoices.append(i.name)
    # labelsChoices = tuple(labelsChoices)
    #tags = ArrayField(models.ForeignKey(Tag), null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="tagged_albums", blank=True)
    labels = models.ManyToManyField(Label, related_name="labeled_albums", blank=True)
    genres = models.ManyToManyField(Genre, related_name='genred_albums', blank=True)
    styles = models.ManyToManyField(Style, related_name='styled_albums', blank=True)
    cover = models.ImageField(width_field=100, height_field=100, blank=True)
    year = models.PositiveIntegerField(verbose_name='year', default=0)
    #жанры, стили, год
#     #image field
#     #from spotify/yandex check

