import unittest

from project.reverse_flask import app

class ConfigTest(unittest.TestCase):
    def test_not_in_debug(self):
        self.assertNotEqual(app.config['DEBUG'], True)

if __name__ == '__main__':
    unittest.main()
