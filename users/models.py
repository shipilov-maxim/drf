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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payday = models.DateTimeField(auto_created=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок', blank=True, null=True)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(choices=CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
