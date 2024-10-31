import requests
from player import Player
from rich import print
from rich.prompt import Prompt
from rich.table import Table


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


def get_season():
    season = Prompt.ask(
        "Select season [bright_magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/bright_magenta]"
    )
    print("")

    seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]

    if season in seasons:
        return season
    else:
        print("Invalid season")
        return None


def get_nationality():
    nationality = Prompt.ask(
        "Select nationality [bright_magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/][/bright_magenta]"
    )
    print("")

    countries = [
        "AUT",
        "CZE",
        "AUS",
        "SWE",
        "GER",
        "DEN",
        "SUI",
        "SVK",
        "NOR",
        "RUS",
        "CAN",
        "LAT",
        "BLR",
        "SLO",
        "USA",
        "FIN",
        "GBR",
    ]

    if nationality in countries:
        return nationality
    else:
        print("Invalid nationality")
        return None


def main():
    print("NHL statistics by nationality \n")

    season = get_season()
    if season == None:
        return

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = get_nationality()

        print(f"Top scorers of {nationality} season {season}")

        if nationality == None:
            return
        players = stats.top_scorers_by_nationality(nationality)

        # for player in players:
        #     print(player)

        table = Table()
        table.add_column("name", style="deep_sky_blue1")
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green3")
        table.add_column("assists", style="green3")
        table.add_column("points", style="green3")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        print(table)

        print("")


if __name__ == "__main__":
    main()
