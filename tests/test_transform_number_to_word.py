import unittest
import sys, os

sys.path.insert(0, os.path.dirname('../numbers_to_word'))
from numbers_to_word.transform_number_to_word import TransformNumbersToWord
from numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException
from numbers_to_word.exceptions.number_not_valid import NumberNotValid


class NumbersTest(unittest.TestCase):

    def test_should_return_dois(self):
        number = 2
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('dois', self.transform_number_to_word.read_number())

    def test_should_return_dez(self):
        number = 10
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('dez', self.transform_number_to_word.read_number())

    def test_should_return_onze(self):
        number = 11
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('onze', self.transform_number_to_word.read_number())

    def test_should_return_quinze(self):
        number = 15
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('quinze', self.transform_number_to_word.read_number())

    def test_should_return_trinta_e_dois(self):
        number = 32
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('trinta e dois', self.transform_number_to_word.read_number())

    def test_should_return_cinquenta(self):
        number = 50
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('cinquenta', self.transform_number_to_word.read_number())

    def test_should_return_noventa_e_nove(self):
        number = 99
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('noventa e nove', self.transform_number_to_word.read_number())

    def test_should_return_cem(self):
        number = 100
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('cem', self.transform_number_to_word.read_number())

    def test_should_return_cento_e_um(self):
        number = 101
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('cento e um', self.transform_number_to_word.read_number())

    def test_should_return_cento_e_quatorze(self):
        number = 114
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('cento e quatorze', self.transform_number_to_word.read_number())

    def test_should_return_cento_e_quarenta(self):
        number = 140
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('cento e quarenta', self.transform_number_to_word.read_number())

    def test_should_return_cento_e_setenta_e_sete(self):
        number = 177
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('cento e setenta e sete', self.transform_number_to_word.read_number())

    def test_should_return_novecentos_e_noventa_e_nove(self):
        number = 999
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('novecentos e noventa e nove', self.transform_number_to_word.read_number())

    def test_should_return_mil(self):
        number = 1000
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('mil', self.transform_number_to_word.read_number())

    def test_should_return_mil_e_um(self):
        number = 1001
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('mil e um', self.transform_number_to_word.read_number())

    def test_should_return_mil_e_oitocentos(self):
        number = 1800
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('mil e oitocentos', self.transform_number_to_word.read_number())

    def test_should_return_nove_mil(self):
        number = 9000
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('nove mil', self.transform_number_to_word.read_number())

    def test_should_return_noventa_e_nove_mil_e_novecentos_e_noventa_e_nove(self):
        number = 94587
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('noventa e quatro mil e quinhentos e oitenta e sete', self.transform_number_to_word.read_number())


    def test_should_return_menos_quarenta_e_dois(self):
        number = -1042
        self.transform_number_to_word = TransformNumbersToWord(number)
        self.assertEqual('menos mil e quarenta e dois', self.transform_number_to_word.read_number())

if __name__ == '__main__':
    unittest.main()
