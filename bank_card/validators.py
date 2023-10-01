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


