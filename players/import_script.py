from players.data.data_20160802 import DATA
from players.models import Player

for p in DATA:
    Player.objects.create(**p)
