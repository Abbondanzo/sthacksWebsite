import unittest
from app import app


class TestSthacksApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        print('SETUP')

    def tearDown(self):
        del self.app

    def test_home_with_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
