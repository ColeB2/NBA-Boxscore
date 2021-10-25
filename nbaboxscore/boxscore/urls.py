from django.urls import path
from . import views
from .views import BoxScoreView, BoxscoreGameView, BoxScoreTodayView, GameSelectView

urlpatterns = [
    path("all", BoxScoreView.as_view(),  name="boxscore-index"),
    path("today", BoxScoreTodayView.as_view(), name="boxscore-index-today"),
    path("", GameSelectView.as_view(), name="game-select"),
    path("game/<int:game_id>", BoxscoreGameView.as_view(), name="game")
    # path("T1", BoxScoreView.as_view(), name="boxscore_indedx1"),
    # path("test", views.boxscore_index1, name="boxscore_index1"),
    # path("test2", views.boxscore_index, name='boxscore_index2'),
]