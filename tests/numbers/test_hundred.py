import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../../service'))
from service.numbers_to_word.numbers.hundred import Hundred


class NumbersTest(unittest.TestCase):

    def test_should_return_prefix_number_from_cento_to_novecentos(self):
        hundred = Hundred()
        numbers = hundred.get_numbers_word()
        for number in range(101, 1000, 100):
            prefix = int(str(number)[0])
            self.assertEqual(numbers[prefix], hundred.get_number_as_word(prefix))

    def test_should_return_prefix_cem(self):
        prefix_one_hundred = 10
        hundred = Hundred()
        self.assertEqual('cem', hundred.get_number_as_word(prefix_one_hundred))


if __name__ == '__main__':
    unittest.main()
