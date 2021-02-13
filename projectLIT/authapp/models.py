from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SiteUser(AbstractUser):
    email = models.CharField(verbose_name='email', max_length=128)
    password = models.CharField(verbose_name='password', max_length=128)
    name = models.CharField(verbose_name='name', max_length=128)
    surname = models.CharField(verbose_name='surname', max_length=128)
    nickname = models.CharField(verbose_name='nickname', max_length=128, unique=True)
    age = models.PositiveIntegerField(verbose_name='age', null=True)
