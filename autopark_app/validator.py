from django.core.exceptions import ValidationError


# plate number validator
# number_example = 'АА 1234 ОО'  # - VALID
# ______________ = '0123456789'


def validate_plate(number):
    #  first check -> length & integers
    if len(number) != 10:
        raise ValidationError(f'{number} is not a correct plate number'
                              f'LengthError')

    if not str.isdigit(number[3:7]):
        raise ValidationError(f'{number} is not a correct plate number'
                              f' NumeralError, middle characters should be numbers')

    #  second check -> spaces & letters
    if not str.isspace(number[2]) or not str.isspace(number[7]):
        raise ValidationError(f'{number} is not a correct plate number'
                              f' ErrorSpace, it should be at least 2 spaces in plate number in correct places'
                              f' example: АА 1234 ОО ')

    if not str.isalpha(number[:2]) or not str.isalpha(number[8:]):
        raise ValidationError(f'{number} is not a correct plate number'
                              f' LettersError, side characters should be letters'
                              f' example: АА 1234 ОО ')

    # third check - > upper case
    if not str.isupper(number[:2]) or not str.isupper(number[8:]):
        raise ValidationError(f'{number} is not a correct plate number'
                              f' LettersUpperError, side characters should be UPPER CASE'
                              f' example: АА 1234 ОО ')


# format received 01-02-2022
# _______________ 0123456789
# _______________ DD-MM-YYYY
# format output   2022-02-01
# _______________ YYYY-MM-DD

def date_format(date):
    date = list(date)
    new_date = []
    for i in date[6:]:
        new_date += i
    new_date += '-'

    for i in date[3:5]:
        new_date += i
    new_date += '-'

    for i in date[:2]:
        new_date += i

    return ''.join(new_date)
