# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def secret_link_email(email, random_string):
    email_template = Template("""
Этот адрес электронной почты был указан при регистрации на сайте Российского Нейтронографического общества

Вот ваша секретная ссылка для подтверждения регистрации:
http://rno.pnpi.spb.ru{% url "members_email_confirm" person.random_string %}

You have received this email because this email address was used during 
registration on the website of the Russian Neutron Scattering Society.
Please follow this link to complete your registration

http://rno.pnpi.spb.ru{% url "members_email_confirm" person.random_string %}

""")
    send_mail(
        "[ РосНейтрО ] Подтверждение регистрации на сайте",
        email_template.render(Context({'person': {'random_string': random_string}})),
        settings.FROM_EMAIL,
        [email],
        fail_silently = False
    )
