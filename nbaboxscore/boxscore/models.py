from django.db import models

# Create your models here.
class Boxscore(models.Model):
    pass

class Player(models.Model):
    game = models.ForeignKey(Boxscore, on_delete=models.CASCADE,null=True)
    first = models.CharField(max_length=30, null=True, default='')
    last = models.CharField(max_length=30, null=True, default='')
    min = models.CharField(max_length=10, null=True, default='')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='PTS')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='FGM')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='FGA')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='3PM')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='3PA')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='FTM')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='FTA')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='+/-')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='OR')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='REB')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='A')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='BLK')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='STL')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='TO')
    pts = models.IntegerField(null=True, blank=True, default=0, verbose_name='PF')
