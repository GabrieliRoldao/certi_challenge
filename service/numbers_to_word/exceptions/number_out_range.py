class NumberIsOutOfRangeException(Exception):
    """
    Exception raised for errors when the input is out of set range

    Attributes:
        number -- input number which caused the error
        message -- explanation about the error
    """

    def __init__(self, number):
        self.number = number
        self.message = f'The input number {self.number} is out of range. Range is between -99999 and 99999!'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.number}'
