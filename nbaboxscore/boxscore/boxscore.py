import requests as req


def get_boxscore_data(game_id):
    game_id = game_id
    url1 = f"https://www.balldontlie.io/api/v1/stats?per_page=100&game_ids[]={game_id}"

    data = req.get(url1)
    return data


class BoxScore(object):
    def __init__(self, game_id=None):
        self.response = get_boxscore_data(game_id)
        self.raw_data = self.response.json()
        # print(f"self.raw_data ----------- {self.raw_data}")

        self.data = self.raw_data['data']

        self.meta = self.raw_data['meta']
        # print(f"self.data ------------------ {self.data}")


        if len(self.data) > 0:
            print(self.data[0])
            self.game_data = self.data[0]['game']
        else:
            self.game_data = None

        try:
            self.hTeam = [player for player in self.data \
                if player['player']['team_id'] == self.game_data['home_team_id']]

            self.vTeam = [player for player in self.data \
                if player['player']['team_id'] == self.game_data['visitor_team_id']]
        except TypeError as e:
            print(e)
            print('Has Occured--------')
            self.hTeam = None
            self.vTeam = None


