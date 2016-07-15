# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.utils.encoding import smart_text
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import Person
import os

class RegistrationTest(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        self.client = Client()
    def tearDown(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'

    def testRegistrationProcess(self):
        response_submit = self.client.post(reverse('members_registration'), 
                {
                    'last_name' : u'тестовая фамилия',
                    'first_name' : u'тестовое имя',
                    'middle_name' : u'тестовое отчество',
            'email': 'test@test123default.org',
            'birthday': '12.01.1996',
            'organization': u'тестовая организация',
            'position': u'тестовая должность',
            'g-recaptcha-response': 'PASSED'
            }, follow=True)
        self.assertEquals(200, response_submit.status_code)
        self.assertNotIn('error', smart_text(response_submit.content))
        self.assertEquals(
                True,
                bool(Person.objects.filter(
                    email = 'test@test123default.org')
                    )
                )
        person = Person.objects.get(email = 'test@test123default.org')
        self.assertNotEquals( "", person.random_string)
        self.assertNotEquals( None, person.random_string)
        response_table = self.client.get(reverse('members_list'))
        content = smart_text(response_table.content)
        self.assertNotIn(u'тестовая фамилия', content)
        self.assertNotIn(u'тестовое имя', content)
        self.assertNotIn(u'тестовое отчество', content)
        self.assertNotIn(u'тестовая организация', content)

        self.assertEquals( None, person.user)

        secret_url = reverse('members_email_confirm', kwargs={'random_string': 'wrongrandomstring'} )
        response_success = self.client.get(secret_url)
        self.assertNotEquals(200, response_success.status_code)
        secret_url = reverse('members_email_confirm', kwargs={'random_string': person.random_string} )
        response_success = self.client.get(secret_url)
        self.assertEquals(200, response_success.status_code)

        person = Person.objects.get(email = 'test@test123default.org')
        self.assertEquals(person.confirmed, True)
        self.assertEquals( True, person.subscribed)
        response_table = self.client.get(reverse('members_list'))
        self.assertIn(u'тестовая фамилия', smart_text(response_table.content))
        self.assertIn(u'тестовое имя', smart_text(response_table.content))
        self.assertIn(u'тестовое отчество', smart_text(response_table.content))
        self.assertIn(u'тестовая организация', smart_text(response_table.content))

        self.assertEquals( User.objects.get(email='test@test123default.org'), person.user )

