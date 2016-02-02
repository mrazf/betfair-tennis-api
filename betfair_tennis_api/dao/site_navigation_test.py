import unittest
import sys
import httpretty
sys.path.append("/Users/farrem09/Projects/betfair-tennis-api")


class TestGettingNavigation(unittest.TestCase):

    @httpretty.activate
    def setUp(self):
        httpretty.register_uri(
            httpretty.POST,
            'https://identitysso.betfair.com/api/certlogin',
            body='poop'
        )

        from betfair_tennis_api import app
        app.config['TESTING'] = True
        self.app = app.test_client()

        import site_navigation

    def test_root_navigation_request_failure_rebuilds_client(self):
        print app.testing
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
