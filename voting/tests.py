# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.utils.encoding import smart_text
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import ValidationError
from members.models import Person, Secret
from .models import Voting, Vote, Candidate
from datetime import datetime
from dateutil.relativedelta import relativedelta


class VotingTestCase(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(
                first_name = 'Imp',
                last_name = 'Lanister',
                middle_name = '-',
                birthday = '2010-01-01',
                email = 'lanister@nosuchemail.uk',
                organization = "King's guard",
                confirmed = True
                )
        self.person2 = Person.objects.create(
                first_name = 'Ramsy',
                last_name = 'Bolton',
                middle_name = 'bastard',
                birthday = '2010-01-01',
                email = 'ramsybolton@nosuchemail.uk',
                organization = "Winterfell",
                confirmed = True
                )
        self.voting = Voting.objects.create(
                name = 'test-votes',
                start_date = datetime.now() + relativedelta(days = -1),
                end_date = datetime.now() + relativedelta(days = 1),
                )
        self.candidate1 = Candidate.objects.create(
                person = self.person1,
                voting = self.voting
                )
        self.candidate2 = Candidate.objects.create(
                person = self.person2,
                voting = self.voting
                )
        self.voting_person = Person.objects.create(
                first_name = 'Sansa',
                last_name = 'Stark',
                middle_name = 'Ned',
                birthday = '2010-01-01',
                email = 'sansastark@nosuchemail.uk',
                organization = "Winterfell",
                confirmed = True
                )
        self.client = Client()
        self.client_outside = Client()
        # request member session
        response = self.client.post(
                reverse('member_request_session'),
                {'email':self.voting_person.email},
                follow = True
                )
        # enter
        secret = Secret.objects.get(user = self.voting_person.user)
        response_enter = self.client.get(
                reverse_lazy(
                    'member_enter',
                    kwargs = {'secret': secret.secret}
                    ),
                follow = True
                )
    def testOutsideClientPageNotAccessible(self):
        response = self.client_outside.get(reverse('votes'))
        self.assertEqual(403, response.status_code)
    def testOutsideClientMenuNotAccessible(self):
        response = self.client_outside.get('/')
        self.assertNotIn(reverse('votes'), smart_text(response.content))

    def testSaveErrorNoOverlapBefore(self):
        Voting.objects.create(
            name = 'before',
            start_date = datetime.now() + relativedelta(days = -5),
            end_date = datetime.now() + relativedelta(days = -4),
            )
    def testSaveErrorOverlapBefore(self):
        try:
            Voting(
                name = 'before_overlap',
                start_date = datetime.now() + relativedelta(days = -2),
                end_date = datetime.now(),
                ).clean()
            self.fail('before_overlap voting created')
        except ValidationError as e:
            self.assertEqual(str(e[0]), 'Период голосования пересекается')
    def testSaveErrorOverlapSmaller(self):
        try:
            Voting(
                name = 'overlap',
                start_date = datetime.now() + relativedelta(hours = -12),
                end_date = datetime.now() + relativedelta(hours = 12),
                ).clean()
            self.fail('overlap voting created')
        except ValidationError as e:
            self.assertEqual(str(e[0]), 'Период голосования пересекается')
    def testSaveErrorOverlapBigger(self):
        try:
            Voting(
                name = 'overlap',
                start_date = datetime.now() + relativedelta(days = -12),
                end_date = datetime.now() + relativedelta(days = 12),
                ).clean()
            self.fail('overlap voting created')
        except ValidationError as e:
            self.assertEqual(str(e[0]), 'Период голосования пересекается')
    def testSaveErrorOverlapAfter(self):
        try:
            Voting(
                name = 'after_overlap',
                start_date = datetime.now(),
                end_date = datetime.now() + relativedelta(days = 2),
                ).clean()
            self.fail('after_overlap voting created')
        except ValidationError as e:
            self.assertEqual(str(e[0]), 'Период голосования пересекается')
    def testSaveErrorNoOverlapAfter(self):
        Voting.objects.create(
            name = 'after',
            start_date = datetime.now() + relativedelta(days = 4),
            end_date = datetime.now() + relativedelta(days = 5),
            )
    def testSaveErrorWrongDates(self):
        try:
            Voting(
                name = 'wrong_date',
                start_date = datetime.now() + relativedelta(days = 15),
                end_date = datetime.now() + relativedelta(days = 10),
                ).clean()
            self.fail('mixed dates voting created')
        except ValidationError as e:
            self.assertEqual(str(e[0]), 'Перепутаны даты начала и конца голосования')

    def testVotesLink(self):
        response = self.client.get('/')
        self.assertIn(reverse('votes'), smart_text(response.content))
    def testVotesPage(self):
        response = self.client.get(
                reverse('votes')
                )
        self.assertIn('candidate', smart_text(response.content))
        self.assertIn(self.person1.first_name, smart_text(response.content))
        self.assertIn(self.person1.last_name, smart_text(response.content))

        self.assertIn(self.person2.first_name, smart_text(response.content))
        self.assertIn(self.person2.last_name, smart_text(response.content))

    def testVotesProcess(self):
        response = self.client.post(
                reverse('votes'),
                {
                    'candidate': self.candidate2.pk
                    },
                follow = True
                )
        self.assertEqual(200, response.status_code)
        self.assertNotIn('error', smart_text(response.content))
        self.assertEqual(0, self.candidate1.vote_set.count())
        self.assertEqual(1, self.candidate2.vote_set.count())

        # check no votes form after the choise
        response_later = self.client.get(reverse_lazy('votes'))
        self.assertNotIn('candidate', smart_text(response_later.content))
