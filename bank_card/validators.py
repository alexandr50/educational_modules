from datetime import datetime

from django.core.exceptions import ValidationError


def validate_card_number(value: str):
    if len(value.strip()) != 19:
        raise ValidationError('Недопустимый номер карты')
    parts_digits = value.split(' ')
    if len(parts_digits) != 4:
        raise ValidationError('Номер катры должен состоять из 16 цифр')
    for item in parts_digits:
        try:
            list(map(lambda x: int(x), item))
        except:
            raise ValidationError('Номер катры должен состоять только из цифр и пробелов')
    return value


def validate_date_card(value: str):
    current_year = str(datetime.now())[2:4]
    current_month = str(datetime.now())[5:7]
    year, month = value.split('/')[1], value.split('/')[0]
    try:
        var = int(year)
        var = int(month)
        var = len(value) == 5
        var = value[2] == '/'
        var = int(current_year) >= int(year)
    except:
        raise ValidationError('Неверная дата')
    if int(year) == int(current_year) and int(current_month) >= int(month):
        raise ValidationError('Неверная дата')
    return value

def validate_csv(value):
    try:
        int(value)
        len(str(value)) == 3
    except:
        ValidationError('Неверный формат')
