import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    # test if player is findable
    def test_findPlayer_exist(self):
        self.assertEqual(
            str(self.stats.search("Kurri")), str(Player("Kurri", "EDM", 37, 53))
        )

    # test that player is not findable when it does not exist
    def test_findPlayer_notexist(self):
        self.assertEqual(self.stats.search("bababui"), None)

    # find all players on the team
    def test_findPlayersOnTeam(self):
        players_of_team = self.stats.team("EDM")

        players_of_team_str = []
        for player in players_of_team:
            players_of_team_str.append(str(player))

        player_list_to_test = [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124",
        ]

        self.assertEqual(players_of_team_str, player_list_to_test)

    # find top players
    def test_top_player(self):
        top_players = self.stats.top(1)

        top_players_str = []
        for player in top_players:
            top_players_str.append(str(player))
        print(top_players_str)

        top_list_to_test = [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
        ]

        self.assertEqual(top_players_str, top_list_to_test)
