import unittest
from project import app

class ReverseTest(unittest.TestCase):

    def setup(self):
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def test_if_user_can_access_the_first_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

    def test_if_page_redirects_and_string_is_reversed(self):
        test_string = 'Hello'
        response = self.app.post('/', data=dict(reverse=test_string, follow_redirects=True))
        self.assertIn(b'olleH',response.data)


    def test_prompt_the_user_to_input_string(self):
        response = self.app.post('/', data=dict(reverse='', follow_redirects=True))
        self.assertIn(b'This field is required', response.data)

    def test_prompt_the_user_to_input_atleast_two_lettered_string(self):
        response = self.app.post('/', data=dict(reverse='h', follow_redirects=True))
        self.assertIn(b'This field is required', response.data)

    
        

