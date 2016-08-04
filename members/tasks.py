# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def confirmation_link_email(email, secret):
    email_template = Template("""
Этот адрес электронной почты был указан при регистрации на сайте Российского Нейтронографического общества

Вот ваша секретная ссылка для подтверждения регистрации:
http://rno.pnpi.spb.ru{% url "members_email_confirm" person.random_string %}

You have received this email because this email address was used during 
registration on the website of the Russian Neutron Scattering Society.
Please follow this link to complete your registration

http://rno.pnpi.spb.ru{% url "members_email_confirm" secret %}

""")
    send_mail(
        "[ РосНейтрО ] Подтверждение регистрации на сайте",
        email_template.render(Context({'secret': secret})),
        settings.FROM_EMAIL,
        [email],
        fail_silently = False
    )

@shared_task
def secret_link_email(email, secret):
    email_template = Template("""
Ссылка для входа на сайт РосНейтрО
https://rno.pnpi.spb.ru{% url "member_enter" secret %}

Действительна в течение двух часов

""")
    send_mail(
        "[ РосНейтрО ] Вход на сайт",
        email_template.render(Context({'secret': secret})),
        settings.FROM_EMAIL,
        [email],
        fail_silently = False
    )

