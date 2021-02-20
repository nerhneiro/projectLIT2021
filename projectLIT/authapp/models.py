from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class SiteUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='age', blank=True)

