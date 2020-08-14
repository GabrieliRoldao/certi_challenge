class Unit:
    def __init__(self):
        self.numbers_and_word = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

    def get_numbers_word(self):
        return self.numbers_and_word

    def get_number_as_word(self, number):
        return self.numbers_and_word[number]
