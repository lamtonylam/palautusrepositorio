from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


class QueryBuilder:
    # eka otetaan matcheriin kaikki pelaajat
    # joka kerta kun esim käytetään plays_in niin pelaajalistaa kierrätetään
    def __init__(self, matcher=All()):
        self._matcher = matcher
        
    def plays_in(self, team):
        return QueryBuilder(PlaysIn(team))

    def has_at_least(self, amount, type):
        return QueryBuilder(And(self._matcher, HasAtLeast(amount, type)))

    def has_fewer_than(self, amount, type):
        return QueryBuilder(And(self._matcher, HasFewerThan(amount, type)))

    def build(self):
        return self._matcher


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query.plays_in("NYR")
        .has_at_least(10, "goals")
        .has_fewer_than(20, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
