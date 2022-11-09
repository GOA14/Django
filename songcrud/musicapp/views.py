from django.shortcuts import render
from .models import Artiste,Song
from .serializers import ArtisteSerializers, SongSerializers
# from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def artiste_list_and_song_list(request):
    if request.method=='GET':
        artiste=Artiste.objects.all()
        song=Song.objects.all()
        art_serializer=ArtisteSerializers(artiste,many=True)
        song_serializer=SongSerializers(song,many=True)

        return Response({'Artiste':art_serializer.data + song_serializer.data})
    if request.method=='POST':
        art_serializer=ArtisteSerializers(data=request.data)
        if art_serializer.is_valid():
            art_serializer.save()
            return Response(art_serializer.data,status=status.HTTP_201_CREATED)
            if song_serializer.is_valid():
                song_serializer.save()
                return Response(song_serializer.data,status=status.HTTP_201_CREATED)

                # To fetch, update and delete  a song in the model
@api_view(['GET', 'PUT', 'DELETE'])
def song_details(request,id):
    try:
        song=Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        song_serializer=SongSerializers(song)
        return Response(song_serializer.data)
    elif request.method=='PUT':
        song_serializer=SongSerializers(song,data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data)
        return Response(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.methodd=='DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # class ArtisteDetailsAPIView(APIView):

    #     def get_object(self, pk):
    #         try:
    #             return Artiste.objects.get(pk=pk)
    #         except Artiste.DoesNotExist:
    #             raise Http404

    #     def get(self, request, pk, fromat=None):
    #         Artiste = self.get_object(pk)
    #         serializer =  ArtisteSerializer(Artiste)
    #         return Response(serializer.data)

    #     def put(self, request, pk, format=None):
    #         Artiste = self.get_object(pk)
    #         serializer =  ArtisteSerializer(Artiste, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     def delete(self, request, pk, format=None):
    #         Artiste = self.get_objects(pk)
    #         Artiste.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)



