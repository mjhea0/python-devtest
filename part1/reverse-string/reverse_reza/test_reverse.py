from reverse import reverse
import unittest


class ReverseTestCase(unittest.TestCase):
    def test(self):
        test_string = "Hello, My name is Reza. Github user name:ni8mr"
        altered_string = "rm8in:eman resu buhtiG .azeR si eman yM ,olleH"
        result_string = reverse(test_string)
        self.assertEqual(altered_string, result_string)

if __name__ == '__main__':
    unittest.main()
