import requests as req
from .scores import Scores, _get_yesterday
from .boxscore import BoxScore

def get_api_req(date=None):
    url = "https://www.balldontlie.io/api/v1/games?dates[]="
    if not date:
        date = _get_yesterday()
    else:
        date = date

    final_url = f"{url}{date[0]}"
    score_data = req.get(final_url)

    return score_data


def get_scoreboard_scores(date=None):
    url = "https://www.balldontlie.io/api/v1/games?dates[]="
    if not date:
        date = _get_yesterday()
    else:
        date = date


    final_url = f"{url}{date[0]}"
    score_data = req.get(final_url)
    score_dict = {}
    game_ids = []

    for game in enumerate(score_data.json()["data"], start=1):
        score_dict[f'G{game[0]}'] = {
            "DATE": date[1],
            "ID":game[1]['id'],
            'HT':game[1]['home_team']['abbreviation'],
            'VT':game[1]['visitor_team']['abbreviation'],
            'HS':game[1]['home_team_score'],
            'VS':game[1]['visitor_team_score']
            }
        game_ids.append(game[1]['id'])

    return score_dict


"""Get Data Functions"""
def create_boxscore_objects():
    """Creates the boxscore objects needed by the views.py file to display the
    data on the website"""
    boxscores = []
    S = Scores()
    for game in S.game_ids:
        if game == None:
            break
        new_boxscore = BoxScore(game_id=game)
        boxscores.append(new_boxscore)
    return boxscores


def split_boxscores(data):
    """Splits the boxscores into a home and away team for easier html table
    management"""
    table_list = []
    for i in range(len(data)):
        table_list.append(data[i].hTeam)
        table_list.append(data[i].vTeam)
    return table_list

def get_boxscores():
    return split_boxscores(create_boxscore_objects())
