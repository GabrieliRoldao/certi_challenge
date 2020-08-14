import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../../service'))
from service.numbers_to_word.numbers.ten import Ten


class NumbersTest(unittest.TestCase):

    def test_should_return_numbers_from_dez_to_noventa(self):
        ten = Ten()
        numbers = ten.get_numbers_word()
        for number in range(1, 10):
            self.assertEqual(numbers[number], ten.get_number_as_word(number))


if __name__ == '__main__':
    unittest.main()
