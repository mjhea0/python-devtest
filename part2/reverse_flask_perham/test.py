# test.py

import unittest

from project import app


class AllTests(unittest.TestCase):

    #############################
    ##### setup and teardown ####
    #############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    #####################
    ##### tests #########
    #####################

    # each test should start with 'test'
    def test_index_page_available(self):
        response = self.app.get('/')
        self.assertIn("Enter a string:", response.data)


    def test_submitted_word_reverses(self):
        response = self.app.post('/', data=dict(string='donkey'))
        self.assertIn("yeknod", response.data)

if __name__ == "__main__":
    unittest.main()

