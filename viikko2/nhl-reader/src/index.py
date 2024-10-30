import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    def return_points(player):
        return player.assists + player.goals

    sorted_players = sorted(players, key=return_points, reverse=True)

    print("Players from FIN \n")

    for player in sorted_players:
        if player.nationality == "FIN":
            print(player)


if __name__ == "__main__":
    main()
