import unittest
from vowel_counter import vowel_counter


class VowelCounterTests(unittest.TestCase):
    def test_vowel_counter(self):
        my_string = 'abracadabra'
        vowel_count = vowel_counter(my_string)
        assert vowel_count == 5

if __name__ == '__main__':
    unittest.main()
