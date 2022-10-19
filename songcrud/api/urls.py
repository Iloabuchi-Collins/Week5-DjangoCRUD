from django.urls import path
from .views import SongList, ArtisteList, SongDetail, LyricsDetail, LyricsList

urlpatterns = [
    path('artiste/', ArtisteList.as_view()),
    path('song/', SongList.as_view()),
    path('song/<int:pk>', SongDetail.as_view()),
    path('lyrics/', LyricsList.as_view()),
    path('lyrics/<int:pk>', LyricsDetail.as_view()),
]