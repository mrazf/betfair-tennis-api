import unittest
import json
import os
import transform


class TestTransform(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        stub = load_stub('./tennis_navigation.json')
        self.transformed = transform.process_root(stub)

    def test_transform_returns_correct_no_of_matches(self):
        size = len(self.transformed)

        self.assertEquals(size, 103)

    def test_transformed_items_have_correct_ids(self):
        from_tournament_one = self.transformed[1]
        from_tournament_two = self.transformed[9]

        self.assertEquals(from_tournament_one['id'], u'27676675')
        self.assertEquals(from_tournament_two['id'], u'27677238')

    def test_transformed_item_has_correct_path(self):
        transformed_item = self.transformed[2]

        self.assertEquals(transformed_item['path'][0], 'Ecuador Open 2016')
        self.assertEquals(transformed_item['path'][1], 'Doubles Matches')
        self.assertEquals(transformed_item['path'][2], 'Maytin/Reyes-Varela v Krajicek/Monroe')


def load_stub(rel_path):
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + rel_path
    with open(abs_path, 'r') as f:
        data = f.read()

    return json.loads(data)


if __name__ == '__main__':
    unittest.main()
