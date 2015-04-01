# Unit Testing

from reverse_function import reverse
import unittest


class TestReverse(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse('hello'), 'olleh')
        self.assertEqual(reverse('newyork'), 'kroywen')
        self.assertNotEqual(reverse('newyork'), 'newyork')


if __name__ == '__main__':
    unittest.main()
