from django.db import models
from django.db import connections
# Create your models here.


class Match(models.Model):
    matchday = models.IntegerField()
    home = models.CharField(max_length=128)
    away = models.CharField(max_length=128)
    score = models.CharField(max_length=128)
    time = models.DateTimeField()
    league_id = models.IntegerField()


    class Meta:
        db_table = "matches"


class League(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "leagues"
