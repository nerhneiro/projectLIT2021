from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
from mainapp.models import Album

class SiteUser(AbstractUser):
    #avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', null=True, blank=True)
    #albums = ArrayField(models.ForeignKey(Album, verbose_name='album', blank=True, on_delete=models.CASCADE), verbose_name='albums')
    albums = models.ManyToManyField(Album, verbose_name='albums', blank=True, related_name='album_users')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=128, blank=True, null=True, verbose_name='country')
    passwordYM = models.CharField(max_length=256, blank=True, verbose_name='Yandex Music password')
    emailYM = models.EmailField(max_length=128, blank=True, verbose_name='yandex Music email')
    # friends = models.ManyToManyField(auth.SiteUser, null=True, verbose_name='friends', related_name='friend_to')