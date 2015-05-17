# test.py


import unittest

from run import app


class TestReverseCase(unittest.TestCase):

    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        # Ensure Flask is setup.
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'please enter some text to reverse...', response.data)

    def test_text_is_reversed(self):
        # Ensure the '/reversed_input/<user_input>' route works.
        response = self.app.get('/reversed_input/FooBar')
        self.assertIn(b'raBooF', response.data)

    def test_form_error(self):
        # Ensure error is populated correctly.
        response = self.app.post('/', data=dict(
            reverse_string='', follow_redirects=True)
        )
        self.assertIn(b'This field is required', response.data)

    def test_functional(self):
        # Ensure form redirects and string is reversed.
        response = self.app.post('/', data=dict(
            reverse_string="Real Python",),  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'nohtyP laeR', response.data)


if __name__ == '__main__':
    unittest.main()
