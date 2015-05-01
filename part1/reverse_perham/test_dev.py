import unittest
import reverse


class TestStringMethod(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse.reverse('donkey'), 'yeknod')

if __name__ == '__main__':
    unittest.main()
