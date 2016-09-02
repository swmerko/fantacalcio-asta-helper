from django.contrib import admin
from players.models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'sold', 'team', 'health', 'player_regularity', 'votes', 'bonus', 'no_malus', 'advice', 'fanta_team', 'sold_value',
    'notes')
    list_filter = ('team', 'role', 'sold')
    list_editable = ('sold', 'fanta_team', 'sold_value')
    search_fields = ('name',)


admin.site.register(Player, PlayerAdmin)



