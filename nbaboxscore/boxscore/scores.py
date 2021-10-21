import datetime
import requests as req



def _get_yesterday():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    display_date = yesterday.strftime("%B %d")
    date_str = f"{yesterday.year}-{yesterday.month}-{yesterday.day}"
    return date_str, display_date


def get_scores(date=None):
    url = f"https://www.balldontlie.io/api/v1/games?dates[]="
    if not date:
        date = _get_yesterday()
    else:
        date = date
    final_url = f"{url}{date[0]}"
    score_data = req.get(final_url)
    return score_data

class Scores(object):
    def __init__(self, date=None):
        self.response = get_scores(date)
        self.raw_data = self.response.json()

        self.data = self.raw_data['data']
        self.meta = self.raw_data['meta']

        self.num_games = self.meta['total_count']

        self.game_ids = []
        self.get_game_ids()

    def get_game_ids(self):
        for game in self.data:
            self.game_ids.append(game['id'])