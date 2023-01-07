from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm, UsernameField
from dataadministrator.models import Character
from django.contrib.auth.models import User

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
