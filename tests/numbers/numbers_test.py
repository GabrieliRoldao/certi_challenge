import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../../numbers_to_word'))
from numbers_to_word.numbers.unit import Unit
from numbers_to_word.numbers.ten import Ten
from numbers_to_word.numbers.teens import Teens
from numbers_to_word.numbers.thousand import Thousand
from numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException


class NumbersTest(unittest.TestCase):

    def test_unit_number_should_return_cinco(self):
        x = 5
        self.assertEqual('cinco', Unit.number_as_word(x))

    def test_unit_number_should_raise_number_out_range_exception(self):
        x = 10
        with self.assertRaises(NumberIsOutOfRangeException): Unit.number_as_word(x)

    def test_teens_number_should_return_dezoito(self):
        x = 8
        self.assertEqual('dezoito', Teens.number_as_word(x))

    def test_ten_number_should_return_cinquenta(self):
        x = 5
        self.assertEqual('cinquenta', Ten.number_as_word(x))

    def test_thousand_number_should_return_trezentos(self):
        x = 3
        self.assertEqual('trezentos', Thousand.number_as_word(x))




if __name__ == '__main__':
    unittest.main()
