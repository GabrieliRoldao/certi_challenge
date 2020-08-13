from numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException


class Hundred:

    @classmethod
    def number_as_word(cls, number):
        numbers_and_word = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
                            'setecentos', 'oitocentos', 'novecentos', 'cem']
        return numbers_and_word[number]
