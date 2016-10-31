# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pages.models import Translation, Translatable
from django.contrib.auth.models import User
import string
import random

def generate_random_string():
    pool = string.letters + string.digits
    return ''.join(random.choice(pool) for i in xrange(50))

class Person(models.Model):
    DEGREES = (
        (u"к.ф.-м.н.", _(u"к.ф.-м.н.")),
        (u"д.ф.-м.н.", _(u"д.ф.-м.н.")),
        (u"к.т.н.", _(u"к.т.н.")),
        (u"д.т.н.", _(u"д.т.н.")),
        (u"к.б.н.", _(u"к.б.н.")),
        (u"д.б.н.", _(u"д.б.н.")),
        (u"к.х.н.", _(u"к.х.н.")),
        (u"д.х.н.", _(u"д.х.н.")),
        (u"к.г.-м.н.", _(u"к.г.-м.н.")),
        (u"д.г.-м.н.", _(u"д.г.-м.н.")),
        (u"к.и.н.", _(u"к.и.н.")),
        (u"д.и.н.", _(u"д.и.н.")),
        (u"к.м.н.", _(u"к.м.н.")),
        (u"д.м.н.", _(u"д.м.н.")),
        (u"к.фарм.н.", _(u"к.фарм.н.")),
        (u"д.фарм.н.", _(u"д.фарм.н.")),
    )
    INTERESTS = (
        ("Biology", _("Biology")),
        ("Chemistry", _("Chemistry")),
        ("Crystallography", _("Crystallography")),
        ("Engineering", _("Engineering")),
        ("Cond. Matter Physics", _("Cond. Matter Physics")),
        ("Fundamental Physics", _("Fundamental Physics")),
        ("Ceramics", _("Ceramics")),
        ("Metallic Materials", _("Metallic Materials")),
        ("Polymers", _("Polymers")),
        ("Other Materials Science", _("Other Materials Science")),
        ("Instrumentation", _("Instrumentation")),
        ("Other", _("Other")),
    )
    MEMBER_EDIT_FIELDS = [
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'email',
            'organization',
            'position',
            'degree',
            ]
    last_name = models.CharField(
            max_length = 255,
            verbose_name = _(u"Фамилия")
    )
    first_name = models.CharField(
            max_length = 255,
            verbose_name = _(u"Имя")
    )
    middle_name = models.CharField(
            max_length = 255,
            verbose_name = _(u"Отчество"),
            blank = True
    )
    birthday = models.DateField(
            verbose_name = _(u"Дата рождения"),
            help_text = _(u"Введите дату в формате дд.мм.гггг или гггг-мм-дд")
    )
    email = models.EmailField(
            verbose_name = _(u"Email")
    )
    organization = models.CharField(
            max_length = 255,
            verbose_name = _(u"Организация")    
    )
    position = models.CharField(
            max_length = 255,
            verbose_name = _(u"Должность")
    )
    degree = models.CharField(
            max_length = 255,
            verbose_name = _(u"Ученая степень"),
            choices = DEGREES,
            blank = True,
    )
    interests = models.CharField(
            max_length = 155,
            verbose_name = _(u"Научные интересы"),
            choices = INTERESTS,
            null = True,
            blank = True
    )
    note = models.TextField(
            verbose_name = _(u"Примечания"),
            null = True,
            blank = True
    )
    publications = models.TextField(
            verbose_name = _(u"Публикации"),
            help_text = _(u"Вы можете просто дать ссылку на свой профиль в Research Gate, или на аналогичный ресурс"),
            blank = True
    )
    approved = models.BooleanField(
            verbose_name = _(u"Подтвержденo право голоса"),
            default = False
    )
    confirmed = models.BooleanField(
            verbose_name = _(u"Подтвердил Email"),
            default = False
    )
    subscribed = models.BooleanField(
            verbose_name = _(u"Подписан на рассылку"),
            default = False
    )
    random_string = models.SlugField(
            max_length = 50,
            verbose_name = _(u"Секретная строка")
    )
    published = models.BooleanField(
            verbose_name = _(u"Опубликован"),
            default = True
    )
    created = models.DateTimeField(
            auto_now_add = True
    )
    updated = models.DateTimeField(
            auto_now = True
    )
    user = models.OneToOneField(User, null=True)
    def __unicode__(self):
        return self.first_name+' '+self.last_name
    def save(self, **kwargs):
        if not self.random_string:
            self.random_string = generate_random_string()
            while Person.objects.filter(
                    random_string = self.random_string
                    ).count() > 0:
                self.random_string = generate_random_string()
        if not self.user and self.confirmed:
            username = self.email[:30]
            self.user = User.objects.create_user(username, self.email)
        return super(Person, self).save(**kwargs)
    class Meta:
        verbose_name = u"Участник"
        verbose_name_plural = u"Участники"
        ordering = ('last_name', 'first_name', 'middle_name',)
    
class Secret(models.Model):
    TIME_TO_LIVE = 24 #hours
    created = models.DateTimeField(
            verbose_name = u"Создан",
            auto_now_add = True
            )
    user = models.ForeignKey(User)
    secret = models.SlugField(
            max_length = 50,
            verbose_name = u"Секрет"
            )
    used = models.BooleanField(
            verbose_name = u"Использован",
            default = False
            )
    def save(self, **kwargs):
        if not self.secret:
            self.secret = generate_random_string()
            while Secret.objects.filter(
                    secret = self.secret
                    ).count() > 0:
                self.secret = generate_random_string()
        if not self.used:
            self.user.set_password(self.secret)
            self.user.save()
        return super(Secret, self).save(**kwargs)
    class Meta:
        verbose_name = u"Секрет для входа"
        verbose_name_plural = u"Секреты для входа"
        ordering = ('-created',)

class CustomEmailMessage(models.Model):
    created = models.DateTimeField(
            verbose_name = u"Создан",
            auto_now_add = True
            )
    subject = models.CharField(
            verbose_name = u"Тема сообщения",
            max_length = 255
            )
    message = models.TextField(
            verbose_name = u"Сообщение"
            )
    subscribers_only = models.BooleanField(
            verbose_name = u"Только подписанным",
            default = True
            )
    attachment1 = models.FileField(
            upload_to = "emailing",
            verbose_name = u"Прикрепленный файл",
            blank = True,
            null = True
            )
    attachment2 = models.FileField(
            upload_to = "emailing",
            verbose_name = u"Прикрепленный файл",
            blank = True,
            null = True
            )
    attachment3 = models.FileField(
            upload_to = "emailing",
            verbose_name = u"Прикрепленный файл",
            blank = True,
            null = True
            )
    sent = models.DateTimeField(
            verbose_name = u"Отправлено",
            null = True,
            default = None
            )
    def __unicode__(self):
        return self.subject
    class Meta:
        verbose_name = u"Сообщение почтовой рассылки"
        verbose_name_plural = u"Сообщения почтовой рассылки"
