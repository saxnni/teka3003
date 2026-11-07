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
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_matching_player(self):
        player = self.stats.search("Lemieux")

        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_when_no_player_matches(self):
        self.assertIsNone(self.stats.search("No such player"))

    def test_team_returns_players_from_requested_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_team_returns_empty_list_when_team_has_no_players(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_returns_players_sorted_by_points(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_returns_empty_list_when_zero_players_requested(self):
        self.assertEqual(self.stats.top(0), [])