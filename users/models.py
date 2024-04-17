from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatar/', verbose_name='Аватар', **NULLABLE)
    token = models.CharField(max_length=35, verbose_name='token', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Статус')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            ('set_active', 'Can active users')
        ]
