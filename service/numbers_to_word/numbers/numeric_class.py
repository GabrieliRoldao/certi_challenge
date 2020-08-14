from abc import ABCMeta, abstractmethod


class NumericClass(metaclass=ABCMeta):

    @abstractmethod
    def get_numbers_word(self):
        pass

    @abstractmethod
    def get_number_as_word(self, number):
        pass
