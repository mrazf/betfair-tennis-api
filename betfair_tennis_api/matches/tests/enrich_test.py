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


def load_stub(rel_path):
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + rel_path
    with open(abs_path, 'r') as f:
        data = f.read()

    return json.loads(data)


if __name__ == '__main__':
    unittest.main()
