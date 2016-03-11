# -*- coding: utf-8 -*-
from django.db import models
from pages.models import Translation, Translatable
import string
import random

def generate_random_string():
    pool = string.letters + string.digits
    return ''.join(random.choice(pool) for i in xrange(50))

class Person(models.Model):
    DEGREES = (
        (u'к.ф.-м.н.', u'к.ф.-м.н.'),
        (u'д.ф.-м.н.', u'д.ф.-м.н.'),
        (u'к.т.н.', u'к.т.н.'),
        (u'д.т.н.', u'д.т.н.'),
        (u'к.б.н.', u'к.б.н.'),
        (u'д.б.н.', u'д.б.н.'),
        (u'к.х.н.', u'к.х.н.'),
        (u'д.х.н.', u'д.х.н.'),
        (u'к.г.-м.н.', u'к.г.-м.н.'),
        (u'д.г.-м.н.', u'д.г.-м.н.'),
        (u'к.и.н.', u'к.и.н.'),
        (u'д.и.н.', u'д.и.н.'),
        (u'к.м.н.', u'к.м.н.'),
        (u'д.м.н.', u'д.м.н.'),
        (u'к.фарм.н.', u'к.фарм.н.'),
        (u'д.фарм.н.', u'д.фарм.н.'),
    )
    first_name = models.CharField(
            max_length = 255,
            verbose_name = "Имя"
    )
    middle_name = models.CharField(
            max_length = 255,
            verbose_name = "Отчество"
    )
    last_name = models.CharField(
            max_length = 255,
            verbose_name = "Фамилия"
    )
    birthday = models.DateField(
            verbose_name = "Дата рождения",
            help_text = "Введите дату в формате дд.мм.гггг или гггг-мм-дд"
    )
    email = models.EmailField(
            verbose_name = "Email"
    )
    organization = models.CharField(
            max_length = 255,
            verbose_name = "Организация"    
    )
    position = models.CharField(
            max_length = 255,
            verbose_name = "Должность"
    )
    degree = models.CharField(
            max_length = 255,
            verbose_name = "Ученая степень",
            choices = DEGREES,
            blank = True,
    )
    interests = models.TextField(
            verbose_name = "Научные интересы",
            blank = True
    )
    note = models.TextField(
            verbose_name = "Примечания",
            null = True,
            blank = True
    )
    publications = models.TextField(
            verbose_name = "Публикации",
            help_text = "Вы можете просто дать ссылку на свой профиль в Research Gate, или на аналогичный ресурс",
            blank = True
    )
    approved = models.BooleanField(
            verbose_name = "Подтвержденo право голоса",
            default = False
    )
    confirmed = models.BooleanField(
            verbose_name = "Подтвердил Email",
            default = False
    )
    subscribed = models.BooleanField(
            verbose_name = "Подтвердил Email",
            default = False
    )
    random_string = models.SlugField(
            max_length = 50,
            verbose_name = "Секретная строка"
    )
    published = models.BooleanField(
            verbose_name = "Опубликован",
            default = True
    )
    created = models.DateTimeField(
            auto_now_add = True
    )
    updated = models.DateTimeField(
            auto_now = True
    )
    def save(self, **kwargs):
        if not self.random_string:
            self.random_string = generate_random_string()
        return super(Person, self).save(**kwargs)
    

