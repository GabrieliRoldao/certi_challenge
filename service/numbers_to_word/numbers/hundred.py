from service.numbers_to_word.numbers.numeric_class import NumericClass


class Hundred(NumericClass):

    def __init__(self):
        self.numbers_and_word = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
                            'setecentos', 'oitocentos', 'novecentos', 'cem']

    def get_numbers_word(self):
        return self.numbers_and_word

    def get_number_as_word(self, number):
        return self.numbers_and_word[number]
