from flask import Blueprint, jsonify
from service.numbers_to_word.transform_number_to_word import TransformNumbersToWord
from service.numbers_to_word.exceptions.number_not_valid import NumberNotValid
from service.numbers_to_word.exceptions.number_out_range import NumberIsOutOfRangeException

number_resource = Blueprint('number_resource', __name__)


@number_resource.route('/<number>')
def show_number(number):
    try:
        number_to_word = TransformNumbersToWord(number)
        return jsonify({'extenso': number_to_word.read_number()}), 200
    except (NumberNotValid, NumberIsOutOfRangeException) as ex:
        return jsonify({'error': ex.message}), 500
    except:
        return jsonify({'error': 'An unexpected error has occurred'}), 500


