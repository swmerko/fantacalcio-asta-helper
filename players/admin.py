from django.contrib import admin
from players.models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'sold', 'team', 'health', 'player_regularity', 'votes', 'bonus', 'no_malus', 'advice', 'my_custom_value',
    'notes')
    list_filter = ('team', 'role', 'sold')
    list_editable = ('sold',)
    search_fields = ('name',)


admin.site.register(Player, PlayerAdmin)



