import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../../service'))
from service.numbers_to_word.numbers.thousand import Thousand


class NumbersTest(unittest.TestCase):

    def test_should_return_mil(self):
        thousand_prefix = 1
        self.assertEqual('mil', Thousand.number_as_word(thousand_prefix))


if __name__ == '__main__':
    unittest.main()
