# Generated by Django 4.2.11 on 2024-05-07 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('pk',), 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
