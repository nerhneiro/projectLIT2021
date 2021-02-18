from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from mainapp.models import Album
class SiteUser(AbstractUser):
    #avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=18)
    albums = models.ManyToManyField(Album, related_name='user_albums', blank=True)