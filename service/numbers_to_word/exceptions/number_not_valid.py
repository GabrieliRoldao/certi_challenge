class NumberNotValid(Exception):
    """
    Exception raised for errors when the input number it's not valid

    Attributes:
        number -- input number which caused the error
        message -- explanation about the error
    """

    def __init__(self, number):
        self.number = number
        self.message = f'The input number {self.number} it\'s not valid. Insert only numbers!!!'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.number}'
