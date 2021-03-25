from django.db import models


# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=100, null=False, blank=False)
    score_available = models.BooleanField(default=False)

    def __str__(self):
        return self.player_name


class Score(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, null=True, blank=True)
    chalk_hit = models.BooleanField(default=False)
    face_hit = models.BooleanField(default=False)
    score = models.PositiveIntegerField(null=True, blank=True, default=0)
    target_hit = models.PositiveIntegerField(null=True, blank=True)
    # oldrank = models.IntegerField(null=True, blank=True, default=0)
    date_played = models.DateTimeField()

    class Meta:
        ordering = ['-date_played']
