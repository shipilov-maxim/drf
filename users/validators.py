from rest_framework.exceptions import ValidationError


class StripePriceValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value[self.field] < 100:
            raise ValidationError('Сумма должна быть не меньше 100')
