from rest_framework.exceptions import ValidationError


class YoutubeURLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field) and 'youtube.com' not in value.get(self.field):
            raise ValidationError('Ссылка должна быть только на Yotube')
