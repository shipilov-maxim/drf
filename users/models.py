from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatar/', verbose_name='Аватар', **NULLABLE)
    token = models.CharField(max_length=35, verbose_name='token', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('set_active', 'Can active users')
        ]


class Billing(models.Model):
    CHOICES = [
        ('CASH', 'Наличными'),
        ('TRANS', 'Перевод на счёт')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)
    payday = models.DateTimeField(auto_created=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(choices=CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='subscriptions',
                               **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
