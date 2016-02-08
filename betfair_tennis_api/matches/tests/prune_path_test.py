import unittest
import os
import json
from .. import enrich
from .. import prune_path as prune


class TestPruning(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        stub = enrich.do(load_stub('raw_match_paths.json'))
        self.pruned = prune.do(stub)

    def test_pruned_path_has_no_tournament(self):
        match_path = self.pruned[0]['path']

        self.assertFalse('Argentina Open 2016' in match_path)

    def test_pruned_path_has_no_players(self):
        match_path = self.pruned[0]['path']

        self.assertFalse('Andujar/Carreno Busta v Cervantes/Lorenzi' in match_path)


def load_stub(rel_path):
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + rel_path
    with open(abs_path, 'r') as f:
        data = f.read()

    return json.loads(data)


if __name__ == '__main__':
    unittest.main()
