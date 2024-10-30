import requests
from player import Player

# reads nhl players from url
class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []

        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)


class PlayerStats:
    def __init__(self, PlayerReader):
        self.PlayerReader = PlayerReader
        self.sorted_players = sorted(
            self.PlayerReader.players, key=self.return_points, reverse=True
        )

    def return_points(self, player):
        return player.assists + player.goals

    def top_scorers_by_nationality(self, nationality):
        self.nationality_players = []
        for player in self.sorted_players:
            if player.nationality == nationality:
                self.nationality_players.append(player)
        return self.nationality_players


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
