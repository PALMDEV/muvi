from __future__ import unicode_literals
from django.contrib.auth.models import  User
from django.db import models

# Create your models here.

# class Game(models.Model):
#     first_player = models.ForeignKey(User, related_name="games_first_player")
#     second_player = models.ForeignKey(User, related_name="games_second_player")
#     next_to_move = models.ForeignKey(User, related_name="games_to_move")
#     start_time = models.DateTimeField(auto_now_add=True)
#     last_active = models.DateTimeField(auto_now=True)
#
# class move(models.Model):
#     x = models.IntegerField()
#     y = models.IntegerField()
#     comment = models.Charfield(max_length=300)
#     game = models.ForeignKey(Game)