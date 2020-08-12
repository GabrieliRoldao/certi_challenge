class Teens:
    
    @classmethod
    def number_as_word(self, number):
        numbers_and_word = ['', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                            'dezoito', 'dezenove']
        return numbers_and_word[number]
