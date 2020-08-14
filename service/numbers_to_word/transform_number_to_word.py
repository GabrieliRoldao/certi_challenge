import re
from service.numbers_to_word.exceptions.number_not_valid import NumberNotValid
from service.numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException
from service.numbers_to_word.numbers.thousand import Thousand
from service.numbers_to_word.numbers.hundred import Hundred
from service.numbers_to_word.numbers.ten import Ten
from service.numbers_to_word.numbers.teens import Teens
from service.numbers_to_word.numbers.unit import Unit


class TransformNumbersToWord:

    def __init__(self, number):
        self.number = number
        self.words = []
        self.group_number_class = 0
        self.negative_number = False
        self.number_as_string = ''
        self.unit = Unit()
        self.ten = Ten()
        self.teens = Teens()
        self.hundred = Hundred()
        self.read_unit = False

    def read_number(self):
        if not self.__is_a_valid_number():
            raise NumberNotValid(self.number)
        if self.__is_number_out_of_range():
            raise NumberIsOutOfRangeException(self.number)

        self.__transform_to_word()
        return ' '.join(self.words).strip()

    def __transform_to_word(self):
        is_only_zero = bool(re.match(r"^0+$", str(self.number)))
        if is_only_zero:
            self.words.append('zero')
        else:
            self.__transform_number_to_string()

            if self.__is_a_negative_number():
                self.negative_number = True
                self.__drop_negative_signal()

            self.__break_number_in_classes()
            self.__fill_number_with_zeros()

            for number in range(0, self.group_number_class * 3, 3):
                hundred, ten, unit = self.__set_hundred_ten_and_unit_numbers(number)
                current_group = self.__get_current_group_number_class(number)

                if number == 0 and self.negative_number:
                    self.words.append('menos')

                if number > 0 and self.__is_sum_hundred_ten_unit_bigger_than_zero(hundred, ten, unit):
                    if len(self.words) > 0:
                        self.__append_letter_e_to_words()

                self.__read_hundred(hundred, ten, unit)
                self.__read_ten(ten, unit)
                if not self.read_unit:
                    self.__read_unit(unit, current_group)

                if self.group_number_class >= 1 and \
                        self.__is_sum_hundred_ten_unit_bigger_than_zero(hundred, ten, unit):
                    self.__append_the_suffix_thousand_to_words(current_group)

    def __is_a_valid_number(self):
        only_number = bool(re.match(r"^-?\d+$", str(self.number)))
        if not only_number:
            raise NumberNotValid(self.number)
        return True

    def __is_number_out_of_range(self):
        return int(self.number) > 99999 or int(self.number) < -99999

    def __transform_number_to_string(self):
        self.number_as_string = str(self.number)

    def __get_number_len(self):
        return len(self.number)

    def __break_number_in_classes(self):
        self.group_number_class = int((len(self.number_as_string) + 2) / 3)

    def __fill_number_with_zeros(self):
        self.number_as_string = self.number_as_string.zfill(self.group_number_class * 3)

    def __set_hundred_ten_and_unit_numbers(self, number):
        return int(self.number_as_string[number]), \
               int(self.number_as_string[number + 1]), \
               int(self.number_as_string[number + 2])

    def __are_ten_and_unit_zero(self, thousand, unit):
        return thousand == 0 and unit == 0

    def __append_letter_e_to_words(self):
        self.words.append('e')

    def __append_number_from_eleven_to_nineteen_to_words(self, teen):
        self.words.append(self.teens.get_number_as_word(teen))

    def __append_the_number_ten_to_words(self, number_ten):
        self.words.append(self.ten.get_number_as_word(number_ten))

    def __append_ten_number_to_words(self, ten_number):
        self.words.append(self.ten.get_number_as_word(ten_number))

    def __append_unit_number_to_words(self, unit_number):
        self.words.append(self.unit.get_number_as_word(unit_number))

    def __append_hundred_number_to_words(self, hundred_number):
        self.words.append(self.hundred.get_number_as_word(hundred_number))

    def __append_the_number_hundred_to_words(self):
        self.words.append(self.hundred.get_number_as_word(10))

    def __append_the_suffix_thousand_to_words(self, current_group):
        self.words.append(Thousand.number_as_word(current_group))

    def __is_sum_hundred_ten_unit_bigger_than_zero(self, hundred, ten, unit):
        return (hundred + ten + unit) > 0

    def __are_hundred_ten_unit_different_from_zero(self, hundred, ten, unit):
        return hundred != 0 and ten != 0 and unit != 0

    def __get_current_group_number_class(self, current_loop_number):
        return int(self.group_number_class - ((current_loop_number / 3) + 1))

    def __is_a_negative_number(self, ):
        return self.number_as_string[0] == '-'

    def __drop_negative_signal(self):
        self.number_as_string = self.number_as_string.split('-')[1]

    def __read_hundred(self, hundred, ten, unit):
        if hundred == 1:
            if self.__are_ten_and_unit_zero(ten, unit):
                self.__append_the_number_hundred_to_words()
            else:
                self.__append_hundred_number_to_words(hundred)
                self.__append_letter_e_to_words()
        elif hundred > 1:
            self.__append_hundred_number_to_words(hundred)
            if ten > 0:
                self.__append_letter_e_to_words()

    def __read_ten(self, ten, unit):
        if ten == 1:
            if unit > 0:
                self.__append_number_from_eleven_to_nineteen_to_words(unit)
                self.read_unit = True
            else:
                self.__append_the_number_ten_to_words(ten)
        elif ten > 1:
            self.__append_ten_number_to_words(ten)
            if unit > 0:
                self.__append_letter_e_to_words()
                self.__append_unit_number_to_words(unit)
                self.read_unit = True

    def __read_unit(self, unit, current_group):
        if unit == 1 and Thousand.number_as_word(current_group) == 'mil':
            pass
        else:
            if unit >= 1:
                self.__append_unit_number_to_words(unit)