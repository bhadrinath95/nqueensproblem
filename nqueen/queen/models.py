from django.db import models

# Create your models here.
class Board(models.Model):
    board_size = models.IntegerField()
    def __str__(self):
        return str(self.board_size)