from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyrics
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

#i need only one serializer per model
class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"
    
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

#prevent the likes and artiste from being updated since they said it's only title and date that's updateable
    def update(self, instance, validated_data):
        if 'likes' or 'artiste_id' in validated_data:    
            validated_data.pop('likes', None)
            validated_data.pop('artiste_id', None)
        return super().update(instance, validated_data)
    
class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = "__all__"
    