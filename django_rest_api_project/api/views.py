from rest_framework import viewsets

from api.serializers import PinBoardsSerializer, NotesSerializer
from api.models import PinBoards, Notes

class PinBoardsViewSet(viewsets.ModelViewSet):
  queryset = PinBoards.objects.all()
  serializer_class = PinBoardsSerializer

class NotesViewSet(viewsets.ModelViewSet):
  queryset = Notes.objects.all()
  serializer_class = NotesSerializer

