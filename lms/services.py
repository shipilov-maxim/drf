from django.core.mail import send_mail
from django.conf import settings


def course_update_email(recipients, course_name):
    send_mail(
        'Изменения в курсе',
        f'{course_name.title()} был изменен.\n',
        settings.EMAIL_HOST_USER,
        recipients,
        fail_silently=True
    )
