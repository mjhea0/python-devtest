from vowel_counter import vowel_counter
import unittest

class VowelCounterTestCase(unittest.TestCase):
    def test(self):
        test_string = "Hello, My name is Reza. Github user name:ni8mr"
        expected_vowel_count = 14
        resulted_vowel_count = vowel_counter(test_string)
        self.assertEqual(expected_vowel_count, resulted_vowel_count)

if __name__=='__main__':
    unittest.main()
