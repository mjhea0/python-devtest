import unittest
from reverse_string import reverse


class ReverseStringTests(unittest.TestCase):
    def test_reverse(self):
        my_string = "testing"
        my_reversed_string = "gnitset"

        returned_string = reverse(my_string)
        assert my_reversed_string == returned_string

if __name__ == "__main__":
    unittest.main()
