from numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException


class Unit:

    @classmethod
    def number_as_word(self, number):
        if number > 9:
            raise NumberIsOutOfRangeException(number)
        numbers_and_word = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        return numbers_and_word[number]