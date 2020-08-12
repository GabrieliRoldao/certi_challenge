from numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException


class Ten:

    @classmethod
    def number_as_word(self, number):
        if number < 10 and number > 90:
            raise NumberIsOutOfRangeException(number)
        numbers_and_word = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta',
                            'oitenta', 'noventa']
        return numbers_and_word[number]
