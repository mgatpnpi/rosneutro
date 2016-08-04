# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.utils.encoding import smart_text
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from .models import Person, Secret
import os

class RegistrationTest(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        self.client = Client()
    def tearDown(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'

    def testRegistrationProcess(self):
        response_submit = self.client.post(
                reverse(
                    'members_registration'
                    ), 
                {
                    'last_name' : u'тестовая фамилия',
                    'first_name' : u'тестовое имя',
                    'middle_name' : u'тестовое отчество',
                    'email': 'test@test123default.org',
                    'birthday': '12.01.1996',
                    'organization': u'тестовая организация',
                    'position': u'тестовая должность',
                    'g-recaptcha-response': 'PASSED'
                    },
                follow=True
                )
        self.assertEquals(200, response_submit.status_code)
        self.assertNotIn('error', smart_text(response_submit.content))
        self.assertEquals(
                True,
                bool(
                    Person.objects.filter(
                        email = 'test@test123default.org'
                        )
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

        secret_url = reverse(
                'members_email_confirm',
                kwargs={
                    'random_string': 'wrongrandomstring'
                    }
                )
        response_success = self.client.get(secret_url)
        self.assertNotEquals(200, response_success.status_code)
        secret_url = reverse(
                'members_email_confirm',
                kwargs={
                    'random_string': person.random_string
                    }
                )
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

        self.assertEquals(
                User.objects.get(
                    email='test@test123default.org'
                    ),
                person.user
                )


class AuthorisationTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
                first_name = 'John',
                last_name = 'Snow',
                middle_name = 'Nedovich',
                birthday = '2010-01-01',
                email = 'johnsnow@nosuchemail.uk',
                organization = "Night's Watch",
                confirmed = True
                )
        os.environ['RECAPTCHA_TESTING'] = 'True'
        self.client = Client()
    def tearDown(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'

    def testUserCreated(self):
        self.assertEqual(self.person.email, self.person.user.email)
    def testWrongEmailRequest(self):
        client = Client()
        response = client.post(
                reverse('member_request_session'),
                {'email': 'notpetrov@nosuchemail123.ru'},
                follow = True
                )
        self.assertIn('error', smart_text(response.content))
        self.assertIn('name="email', smart_text(response.content))
    def testMemberEnterProcess(self):
        # request member session
        response = self.client.post(
                reverse('member_request_session'),
                {'email':self.person.email},
                follow = True
                )
        self.assertEqual(200, response.status_code)
        self.assertNotIn('error', smart_text(response.content))

        # blocked request for member session
        response = self.client.post(
                reverse('member_request_session'),
                {'email':self.person.email},
                follow = True
                )
        self.assertIn('error', smart_text(response.content))
        self.assertIn('<input', smart_text(response.content))
        # enter
        secret = Secret.objects.get(user = self.person.user)
        response_enter = self.client.get(
                reverse_lazy(
                    'member_enter',
                    kwargs = {'secret': secret.secret}
                    ),
                follow = True
                )
        self.assertEqual(200, response_enter.status_code)
        self.assertEqual(
                self.person.user.email,
                response_enter.context['user'].email
                )
        test_response = self.client.get('/')
        self.assertEqual(200, test_response.status_code)
        self.assertEqual(
                self.person.user.email,
                test_response.context['user'].email
                )


        # logout
        response_enter = self.client.get(
                reverse_lazy('member_logout'),
                follow = True
                )
        self.assertEqual(200, response_enter.status_code)
        self.assertEqual(
                False,
                hasattr(response_enter.context, 'user')
                )
        response = self.client.post(
                reverse('member_request_session'),
                {'email':self.person.email},
                follow = True
                )
        self.assertNotIn('error', smart_text(response.content))
    def testWrongEnterAttempt(self):
        response_enter = self.client.get(
                reverse_lazy(
                    'member_enter',
                    kwargs = {'secret': 'nosuchsecret'}
                    ),
                follow = True
                )
        self.assertEqual(404, response_enter.status_code)
    def testExpiredSecretEnter(self):
        # request member session
        response = self.client.post(
                reverse('member_request_session'),
                {'email':self.person.email},
                follow = True
                )
        self.assertEqual(200, response.status_code)

        # enter
        secret = Secret.objects.get(user = self.person.user)
        secret.created = secret.created - relativedelta(hours = Secret.TIME_TO_LIVE + 1)
        secret.save()
        response_enter = self.client.get(
                reverse_lazy(
                    'member_enter',
                    kwargs = {'secret': secret.secret}
                    ),
                follow = True
                )
        self.assertEqual(404, response_enter.status_code)
