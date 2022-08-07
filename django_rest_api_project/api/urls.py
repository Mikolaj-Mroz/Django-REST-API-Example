import imp
from operator import imod
from django.urls import include, path

from rest_framework import routers

from api.views import PinBoardsViewSet, NotesViewSet

router = routers.DefaultRouter()
router.register(r'pinboards', PinBoardsViewSet)
router.register(r'notes', NotesViewSet)

urlpatterns = [
  path('', include(router.urls)),
]