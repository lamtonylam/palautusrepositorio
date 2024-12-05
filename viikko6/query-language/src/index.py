from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(70, "points"), Or(PlaysIn("NYR"), PlaysIn("FLA"), PlaysIn("BOS"))
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
