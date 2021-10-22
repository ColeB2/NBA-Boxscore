# from django.shortcuts import render
from django.views.generic.base import TemplateView

from .custom import get_boxscores, get_scoreboard_scores
from .customtest import get_api_reqTEST, get_scoreboard_scoresTEST, get_boxscoresT
import datetime




"""Views"""
class BoxScoreView(TemplateView):
    template_name = "boxscore/boxscore_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scores'] = get_scoreboard_scores()
        context['boxscores'] = get_boxscores()
        return context


class BoxScoreTodayView(TemplateView):
    template_name = "boxscore/boxscore_index_today.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.date.today()
        display_date = today.strftime("%B %d")
        date_str = f"{today.year}-{today.month}-{today.day}"
        resp_data = get_api_reqTEST(date_str)
        # print(f"date tsr {date_str} respdata {resp_data}")

        context['scores'] = get_scoreboard_scoresTEST(resp_data, (date_str,display_date))
        context['boxscores'] = get_boxscoresT(resp_data)
        return context


class GameSelectView(TemplateView):
    template_name = "boxscore/game_select.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scores'] = get_scoreboard_scores()
        return context


class BoxscoreGameView(TemplateView):
    template_name = "boxscore/game_view.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scores'] = get_scoreboard_scores()
        return context








