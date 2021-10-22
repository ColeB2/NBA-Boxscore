from django.urls import path
from . import views
from .views import BoxScoreView, BoxScoreTodayView, GameSelectView

urlpatterns = [
    path("", BoxScoreView.as_view(),  name="boxscore_index"),
    path("today", BoxScoreTodayView.as_view(), name="boxscore_index_today"),
    path("select", GameSelectView.as_view(), name="game-select"),
    # path("T1", BoxScoreView.as_view(), name="boxscore_indedx1"),
    # path("test", views.boxscore_index1, name="boxscore_index1"),
    # path("test2", views.boxscore_index, name='boxscore_index2'),
]