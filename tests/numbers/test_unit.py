import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../../service'))
from service.numbers_to_word.numbers.unit import Unit


class NumbersTest(unittest.TestCase):

    def test_should_return_numbers_from_um_to_nove(self):
        unit = Unit()
        numbers = unit.get_numbers_word()
        for number in range(1, 10):
            self.assertEqual(numbers[number], unit.get_number_as_word(number))


if __name__ == '__main__':
    unittest.main()
