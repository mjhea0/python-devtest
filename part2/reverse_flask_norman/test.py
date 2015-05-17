# tests

from project import app
import unittest


class ReverseCase(unittest.TestCase):

    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_homepage_exists(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Reverse this text', response.data)

    def test_text_is_reversed(self):
        response = self.app.get('/reversed_input/HelloWorld')
        self.assertIn(b'dlroWolleH', response.data)

    def test_users_must_enter_string(self):
        response = self.app.post(
            '/',
            data=dict(reverse='', follow_redirects=True)
        )
        self.assertIn(b'This field is required', response.data)

    def test_redirects_to_output(self):
        response = self.app.post(
            '/',
            data=dict(reverse="Hello",),  follow_redirects=True)
        self.assertIn(b'olleH', response.data)

if __name__ == '__main__':
    unittest.main()
