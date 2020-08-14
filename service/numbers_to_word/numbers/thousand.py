class Thousand:

    @classmethod
    def number_as_word(cls, number):
        numbers_and_word = ['', 'mil', 'milhão']
        return numbers_and_word[number]
