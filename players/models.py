from django.db import models


class Player(models.Model):
    """
    Player model
    """
    team = models.CharField(max_length=256)
    role = models.CharField(max_length=3)
    name = models.CharField(max_length=256)
    health = models.IntegerField(default=0)
    player_regularity = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    no_malus = models.IntegerField(default=0)
    advice = models.IntegerField(default=0)
    my_custom_value = models.IntegerField(default=0)
    notes = models.CharField(max_length=256)
    sold = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
