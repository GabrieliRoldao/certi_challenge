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

    def read_number(self):
        if not self.is_a_valid_number():
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
            self.fill_number_with_zeros()

            for x in range(0, self.group_number_class * 3, 3):
                hundred = self.cast_to_int(self.number_as_string[x])
                ten = self.cast_to_int(self.number_as_string[x + 1])
                unit = self.cast_to_int(self.number_as_string[x + 2])
                current_group = self.__get_current_group_number_class(x)

                if x == 0:
                    if self.negative_number:
                        self.words.append('menos')

                if x > 0 and self.__is_sum_hundred_ten_unit_bigger_than_zero(hundred, ten, unit):
                    self.__append_letter_e_to_words()

                if hundred == 1:
                    if self.are_ten_and_unit_zero(ten, unit):
                        self.__append_the_number_hundred()
                    else:
                        self.__append_hundred_number(hundred)
                        self.__append_letter_e_to_words()
                elif hundred > 1:
                    self.__append_hundred_number(hundred)
                    if ten > 0:
                        self.__append_letter_e_to_words()
                if ten == 1:
                    if unit > 0:
                        self.__append_number_from_eleven_to_nineteen(unit)
                    else:
                        self.__append_the_number_ten(ten)
                elif ten > 1:
                    self.__append_ten_number(ten)
                    if unit > 0:
                        self.__append_letter_e_to_words()
                        self.__append_unit_number(unit)
                else:
                    if unit == 1 and Thousand.number_as_word(current_group) == 'mil':
                        pass
                    else:
                        if unit >= 1:
                            self.__append_unit_number(unit)
                if self.group_number_class >= 1 and \
                        self.__is_sum_hundred_ten_unit_bigger_than_zero(hundred, ten, unit):
                    self.__append_the_suffix_thousand(current_group)

    def is_a_valid_number(self):
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

    def fill_number_with_zeros(self):
        self.number_as_string = self.number_as_string.zfill(self.group_number_class * 3)

    def are_ten_and_unit_zero(self, thousand, unit):
        return thousand == 0 and unit == 0

    def cast_to_int(self, number_to_cast):
        return int(number_to_cast)

    def __append_letter_e_to_words(self):
        self.words.append('e')

    def __append_number_from_eleven_to_nineteen(self, teen):
        self.words.append(self.teens.get_number_as_word(teen))

    def __append_the_number_ten(self, number_ten):
        self.words.append(self.ten.get_number_as_word(number_ten))

    def __append_ten_number(self, ten_number):
        self.words.append(self.ten.get_number_as_word(ten_number))

    def __append_unit_number(self, unit_number):
        self.words.append(self.unit.get_number_as_word(unit_number))

    def __append_hundred_number(self, hundred_number):
        self.words.append(self.hundred.get_number_as_word(hundred_number))

    def __append_the_number_hundred(self):
        self.words.append(self.hundred.get_number_as_word(10))

    def __append_the_suffix_thousand(self, current_group):
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
