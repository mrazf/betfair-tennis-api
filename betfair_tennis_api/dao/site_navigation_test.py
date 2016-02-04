import unittest
import sys
import httpretty
import os
from mock import patch
from betfair import Betfair
sys.path.append("/Users/farrem09/Projects/betfair-tennis-api")


class TestGettingNavigation(unittest.TestCase):

    @httpretty.activate
    def setUp(self):
        httpretty.register_uri(
            httpretty.POST,
            'https://identitysso.betfair.com/api/certlogin',
            body=loadStub('successful_login_resp.json')
        )

        from betfair_tennis_api import app

        app.config['TESTING'] = True
        app.config['BETFAIR_USER_NAME'] = 'usrnme'
        app.config['BETFAIR_PASSWORD'] = 'psswrd'
        self.app = app.test_client()

    @httpretty.activate
    @patch.object(Betfair, 'login')
    def test_navigation_request_failure_rebuilds_client(self, mock):
        from site_navigation import get_navigation

        httpretty.register_uri(
            httpretty.GET,
            'https://api.betfair.com/exchange/betting/rest/v1/en/navigation/menu.json',
            body=loadStub('failed_navigation_resp.json')
        )

        with self.app.application.app_context():
            get_navigation()

        mock.assert_called_once_with('usrnme', 'psswrd')

    def test_navigation_request_failure_retrys_with_new_session_token(self):
        pass


def loadStub(rel_path):
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + rel_path
    with open(abs_path, 'r') as f:
        data = f.read()

    return data

if __name__ == '__main__':
    unittest.main()
