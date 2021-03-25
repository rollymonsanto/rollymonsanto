from django.contrib import admin
from .models import Score, Player

admin.site.site_header = 'BeefWeek Whip Cracking Admin'
admin.site.site_title = 'Admin'
# admin.site.site_url = 'https://www.builddirector.com/'
admin.site.index_title = 'Administration'
admin.empty_value_display = '**Empty**'


class ScoreAdmin(admin.ModelAdmin):
    fields = ('date_played', 'player', 'score', 'chalk_hit', 'face_hit', 'target_hit')
    list_display = ('date_played', 'player', 'score', 'chalk_hit', 'face_hit', 'target_hit')
    list_display_links = ('score', 'date_played')
    ordering = ('-date_played',)
    list_editable = ('player', 'face_hit', 'target_hit')


class PlayerAdmin(admin.ModelAdmin):
    # fields = ('id', 'player_name')
    list_display = ('id', 'player_name', 'score_available')
    ordering = ('-id',)
    list_editable = ('player_name',)


admin.site.register(Score, ScoreAdmin)
admin.site.register(Player, PlayerAdmin)
