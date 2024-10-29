from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader


def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")
    )
    philadelphia_flyers_players = stats.team("PHI")
    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    for player in stats.top(10, SortBy.POINTS):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)


if __name__ == "__main__":
    main()
