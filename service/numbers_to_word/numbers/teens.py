from service.numbers_to_word.numbers.numeric_class import NumericClass


class Teens(NumericClass):

    def __init__(self):
        self.numbers_and_word = ['', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                            'dezoito', 'dezenove']

    def get_numbers_word(self):
        return self.numbers_and_word

    def get_number_as_word(self, number):
        return self.numbers_and_word[number]
