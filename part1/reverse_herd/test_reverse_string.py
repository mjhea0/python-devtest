from reverse_string import reverse
import unittest


class ReverseStringTest(unittest.TestCase):

    # setUp
    # helpers

    # tests
    def test_string_is_reversed(self):
        test_str = 'rabbit'
        result_expected = 'tibbar'
        result_actual = reverse(test_str)
        self.assertEqual(result_expected, result_actual)


if __name__ == '__main__':
    unittest.main()
