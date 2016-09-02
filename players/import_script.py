from players.data.data_20160802 import DATA
from players.models import Player

for p in DATA:
    Player.objects.create(**p)


for p in Player.objects.all():
    p.name = p.name.capitalize()
    p.save()
