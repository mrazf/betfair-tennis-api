import unittest
import os
import json
from .. import enrich


class TestEnrichment(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.enriched = enrich.do(load_stub('raw_match_paths.json'))

    def test_enriched_match_has_correct_players_one_and_two(self):
        player_one = self.enriched[0]['playerOne']
        player_two = self.enriched[0]['playerTwo']

        self.assertEquals(player_one, 'Andujar/Carreno Busta')
        self.assertEquals(player_two, 'Cervantes/Lorenzi')

    def test_enriched_match_has_correct_tournament(self):
        tournament = self.enriched[0]['tournament']

        self.assertEquals(tournament, "Argentina Open 2016")

    def test_enriched_matches_have_correct_singles_status(self):
        match_one = self.enriched[0]
        match_two = self.enriched[7]

        self.assertEquals(match_one['singles'], False)
        self.assertEquals(match_two['singles'], True)

    def test_enriched_matches_have_mens_true_if_in_path(self):
        match = self.enriched[106]

        self.assertEquals(match['mens'], True)

    def test_enriched_matches_have_mens_false_if_women_in_path(self):
        match = self.enriched[105]

        self.assertFalse(match['mens'])


def load_stub(rel_path):
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + rel_path
    with open(abs_path, 'r') as f:
        data = f.read()

    return json.loads(data)


if __name__ == '__main__':
    unittest.main()
