# Generated by Django 4.2.11 on 2024-04-17 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview/', verbose_name='Превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview/', verbose_name='Превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('url_video', models.URLField(verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]