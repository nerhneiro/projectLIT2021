from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#
class SiteUser(AbstractUser):
    name = models.CharField(verbose_name='name', max_length=128, default='User')
    password = models.CharField(verbose_name='password', max_length=128, default='-1')
    email = models.CharField(verbose_name='email', max_length=128, default='email@email.ru')