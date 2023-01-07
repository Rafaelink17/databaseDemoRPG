from django.shortcuts import render
from dataadministrator.models import Character
from dataadministrator.forms import CharacterForm


from django.http import JsonResponse
from dataadministrator.serializers import CharacterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return render(request, 'dataadministrator/index.html')



def createCharacter(request):
    if request.method == 'POST':
        character = CharacterForm(data=request.POST)
        if character.is_valid():
            character.save()
    return render(request, 'dataadministrator/register.html')

def createCharacterForm(request):
    character = CharacterForm(request.POST)
    if character.is_valid():
        character.save()
    return render(request, 'dataadministrator/index.html')




def showCharacters(request):
    characters = Character.objects.all()
    data = {'characters':list(characters.values('name','level'))}
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def listCharacters(request):
    if request.method == 'GET':
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CharacterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def empleados_detail(request, pk):

    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def listarEmpleados(request):
    empleados = Empleado.objects.all()
    data = {'empleados':list(empleados.values('nombre','salario'))}
    return JsonResponse(data)