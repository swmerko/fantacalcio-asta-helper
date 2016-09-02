from django.db import models


class Team(models.Model):
    """
    Player model
    """
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name