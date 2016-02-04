import unittest
import json
import os
import transform


class TestTransform(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        stub = load_stub('./tennis_navigation.json')
        self.transformed = transform.take_root(stub)

    def test_transform_returns_correct_no_of_matches(self):
        size = len(self.transformed)

        self.assertEquals(size, 103)

    def test_transformed_item_has_correct_id(self):
        transformed_item = self.transformed[1]

        self.assertEquals(transformed_item['id'], u'27676675')

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
