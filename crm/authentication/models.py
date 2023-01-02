from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.IntegerField(blank=False, null=True)
    user_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=400, blank=True)
    password = models.CharField(max_length=255, blank=True)
