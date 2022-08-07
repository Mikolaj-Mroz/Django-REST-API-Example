from django.db import models

# Create your models here.



class PinBoards(models.Model):
  RED = '255, 0, 0'
  GREEN = '0, 255, 0'
  BLUE = '0, 0, 255'
  COLORS = [
    (RED, 'Red'),
    (GREEN, 'Green'),
    (BLUE, 'Blue')
  ]
  name = models.CharField(max_length=100)
  color = models.CharField(
    max_length=9,
    choices=COLORS,
    default=RED,
  )
  

class Notes(models.Model):
  YES = 'true'
  NO = 'false'
  DONE = [
    (YES, 'Yes'),
    (NO, 'No')
  ]
  title = models.CharField(max_length=30)
  content = models.CharField(max_length=800)
  done = models.CharField(
    max_length=5,
    choices=DONE,
    default=NO
  )
  pin_board = models.ForeignKey(PinBoards, on_delete=models.DO_NOTHING)