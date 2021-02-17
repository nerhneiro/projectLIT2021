from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from ..mainapp.models import Album, Artist, Label, Tag

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=18)
    albums = ArrayField(models.ForeignKey(Album, verbose_name='album', blank=True), verbose_name='albums')