from rest_framework import serializers

from api.models import PinBoards, Notes

class PinBoardsSerializer(serializers.ModelSerializer):
   class Meta:
       model = PinBoards
       fields = ('name', 'color')

class NotesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Notes
       fields = ('title', 'content', 'done', 'pin_board')