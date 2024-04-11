from django.contrib.auth.models import User
from django.db import models


class PopularColor(models.Model):
    name = models.CharField(max_length=255)
    hue = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)


class UserColors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hue = models.IntegerField()
    sat = models.IntegerField()
    lightness = models.IntegerField()
    hex = models.CharField(max_length=10)
