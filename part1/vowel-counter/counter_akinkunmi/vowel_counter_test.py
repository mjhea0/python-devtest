from vowel_counter import vowel_counter
import unittest


class VowelCounterTestCase(unittest.TestCase):
    def test(self):
        test_string = "Akinkunmi"
        expected_vowel_count = {'a': 1, 'i': 1, 'u': 1}
        resulted_vowel_count = vowel_counter(test_string)
        self.assertEqual(expected_vowel_count, resulted_vowel_count)

if __name__ == '__main__':
    unittest.main()
