from django.shortcuts import get_object_or_404
from urllib import response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import MusicSerializer
from music_library import serializers

@api_view(['GET', 'POST'])
def music_library_list(request):

    if request.method == 'GET':
        song = Song.objects.all()
        serializer = MusicSerializer(song, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def music_library_detail(request, pk):

    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(song)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MusicSerializer(song, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
