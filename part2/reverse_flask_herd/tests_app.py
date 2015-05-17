import unittest

from project.reverse_flask import app



class AppTest(unittest.TestCase):
    # helper methods

    ##########################
    ### setup and teardown ###
    ##########################

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()


    #############
    ### tests ###
    #############

    def test_index_page_renders(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter the string to reverse', response.data)

    def test_reverse_string_page_renders(self):
        test_string = 'rabbit'
        expected_string = 'tibbar'
        response = self.app.post('/reverse_string', data=dict(
            str_to_reverse=test_string)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected_string, response.data)


if __name__ == '__main__':
    unittest.main()