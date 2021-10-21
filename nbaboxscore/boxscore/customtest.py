import requests as req
from .scores import _get_yesterday
from .boxscore import BoxScore

def get_api_reqTEST(date=None):
    """
    params:
        date: date str --> YYYY-MM-DD format
    """
    url = f"https://www.balldontlie.io/api/v1/games?dates[]="
    if not date:
        date = _get_yesterday()
    else:
        date = date

    final_url = f"{url}{date}"
    score_data = req.get(final_url)
    # print(f"req score data {score_data}")

    return score_data


def get_scoreboard_scoresTEST(response_data, date):
    score_data = response_data
    score_dict = {}

    for game in enumerate(score_data.json()["data"], start=1):
        score_dict[f'G{game[0]}'] = {
            "DATE": date[1],
            "ID":game[1]['id'],
            'HT':game[1]['home_team']['abbreviation'],
            'VT':game[1]['visitor_team']['abbreviation'],
            'HS':game[1]['home_team_score'],
            'VS':game[1]['visitor_team_score']
            }

    return score_dict


"""Get Data Functions"""
def create_boxscore_objectsT(response_data):
    """Creates the boxscore objects needed by the views.py file to display the
    data on the website"""
    boxscores = []
    S = ScoresTest(response_data)
    for game in S.game_ids:
        if game == None:
            break
        new_boxscore = BoxScore(game_id=game)
        boxscores.append(new_boxscore)
    return boxscores


def split_boxscoresT(data):
    """Splits the boxscores into a home and away team for easier html table
    management"""
    table_list = []
    for i in range(len(data)):
        table_list.append(data[i].hTeam)
        table_list.append(data[i].vTeam)
    return table_list

def get_boxscoresT(response_data):
    return split_boxscoresT(create_boxscore_objectsT(response_data))


class ScoresTest(object):
    def __init__(self, response_data):
        self.response = response_data
        self.raw_data = self.response.json()

        self.data = self.raw_data['data']
        self.meta = self.raw_data['meta']

        self.num_games = self.meta['total_count']

        self.game_ids = []
        self.get_game_ids()

        # self.score_dict = {}
        # self.create_scoreboard()

    def get_game_ids(self):
        for game in self.data:
            self.game_ids.append(game['id'])

    # def create_scoreboard(self):
    #     for game in enumerate(self.data, start=1):
    #         self.score_dict[f'G{game[0]}'] = {
    #         "DATE": self.date[1],
    #         "ID":game[1]['id'],
    #         'HT':game[1]['home_team']['abbreviation'],
    #         'VT':game[1]['visitor_team']['abbreviation'],
    #         'HS':game[1]['home_team_score'],
    #         'VS':game[1]['visitor_team_score']
    #         }