import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../../service'))
from service.numbers_to_word.numbers.teens import Teens


class NumbersTest(unittest.TestCase):

    def test_should_return_numbers_from_onze_to_dezenove(self):
        teens = Teens()
        numbers = teens.get_numbers_word()
        for number in range(1, 10):
            self.assertEqual(numbers[number], teens.get_number_as_word(number))


if __name__ == '__main__':
    unittest.main()
