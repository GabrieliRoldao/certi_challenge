class NumberIsOutOfRangeException(Exception):
    """
    Exception raised for errors when the input is out of set range

    Attributes:
        number -- input number which caused the error
        message -- explanation about the error
    """

    def __init__(self, number, message='The input number is out of range'):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.number}'
