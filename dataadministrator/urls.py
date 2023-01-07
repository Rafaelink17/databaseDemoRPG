from django.urls import path
from dataadministrator.views import index, createCharacter, createCharacterForm,showCharacters
urlpatterns = [
    path('index', index),
    path('createCharacter', createCharacter),
    path('createCharacterForm', createCharacterForm),
    path('character/showCharacters', showCharacters),
]
