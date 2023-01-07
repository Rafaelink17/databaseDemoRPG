from rest_framework import serializers
from dataadministrator.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'