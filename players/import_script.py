from players.data.data_2016 import DATA
from players.models import Player

for p in DATA:
    Player.objects.create(**p)
    try:
        Player.objects.create(**p)
    except Exception as exc:
        print p['name']
