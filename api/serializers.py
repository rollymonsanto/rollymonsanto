from rest_framework import serializers
from ranking.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('date_played', 'score', 'chalk_hit', 'target_hit')
