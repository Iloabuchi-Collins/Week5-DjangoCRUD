from rest_framework import generics
from musicapp.models import Artiste, Song, Lyrics
from .serializers import ArtisteSerializer, SongSerializer, LyricsSerializer

# Create your views here.

class SongList(generics.ListCreateAPIView):
	serializer_class = SongSerializer

	def get_queryset(self):
		queryset = Song.objects.all()
		artiste = self.request.query_params.get('artiste')
		if artiste is not None:
		    queryset = queryset.filter(artiste_id = artiste)
		return queryset

class ArtisteList(generics.ListCreateAPIView):
	queryset = Artiste.objects.all()
	serializer_class = ArtisteSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer 

class LyricsDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Lyrics.objects.all()
	serializer_class = LyricsSerializer

class LyricsList(generics.ListCreateAPIView):
	serializer_class = LyricsSerializer

	def get_queryset(self):
		queryset = Lyrics.objects.all()
		song = self.request.query_params.get('song')
		if song is not None:
		    queryset = queryset.filter(song_id = song)
		return queryset