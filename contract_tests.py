import unittest
import requests
import json

class TestContracts(unittest.TestCase):

    def test_what_is_a_contract(self):
        "An attempt to work this out"

        live_swagger = json.loads(requests.get("https://crackling-fire-5301.firebaseapp.com/api.json").text)
        with open('swagger.json', 'r') as f:
            this_swagger = json.loads(f.read())

        self.assertEquals(live_swagger['info']['version'], this_swagger['info']['version'])


if __name__ == '__main__':
    unittest.main()
