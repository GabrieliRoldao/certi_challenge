from numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException


class Thousand:

    @classmethod
    def number_as_word(self, number):
        numbers_and_word = ['', 'cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
                            'setecentos', 'oitocentos', 'novecentos']
        return numbers_and_word[number]