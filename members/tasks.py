# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def secret_link_email(person):
    email_template = Template("""
Этот адрес электронной почты был указан при регистрации на сайте Российского Нейтронографического общества

Вот секретная ссылка для подтверждения регистрации:
http://rno.pnpi.spb.ru{% url "members_email_confirm" person.random_string %}


""")
    send_mail(
        "[ РосНейтрО ] Подтверждение регистрации на сайте",
        email_template.render(Context({'person': person})),
        settings.FROM_EMAIL,
        [person.email],
        fail_silently = False
    )
    return True
