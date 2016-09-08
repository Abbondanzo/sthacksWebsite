import unittest
from app import app
from config import locations
from freezegun import freeze_time
from v1.sunset import url
import httpretty


class TestSthacksApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        del self.app

    @freeze_time("2016-09-10 8:00:01")
    @httpretty.activate
    def test_home_not_sunset(self):
        httpretty.register_uri(httpretty.GET, url,
                               body='{"results": {"civil_twilight_end": "11:33:27 PM"}}',
                               content_type="application/json")
        response = self.app.get('/')
        text = response.data
        self.assertEqual(response.status_code, 403)
        self.assertIn("Try again later", text)

    @freeze_time("2016-09-7 11:32:27")
    @httpretty.activate
    def test_home_with_sunset(self):
        httpretty.register_uri(httpretty.GET, url,
                               body='{"results": {"civil_twilight_end": "11:33:27 PM"}}',
                               content_type="application/json")
        response = self.app.get('/')
        text = response.data
        self.assertEqual(response.status_code, 200)
        self.assertIn(locations[0], text)
