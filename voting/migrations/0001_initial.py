# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_auto_20160816_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.ForeignKey(verbose_name='\u0427\u0435\u043b\u043e\u0432\u0435\u043a \u0438\u0437 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432', to='members.Person')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442',
                'verbose_name_plural': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate', models.ForeignKey(to='voting.Candidate')),
                ('person', models.ForeignKey(to='members.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0435 \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('start_date', models.DateTimeField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('end_date', models.DateTimeField(null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='VotingTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=7, verbose_name=b'\xd0\xaf\xd0\xb7\xd1\x8b\xd0\xba', choices=[(b'ru', 'Russian'), (b'en', 'English')])),
                ('description', redactor.fields.RedactorField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('parent', models.ForeignKey(related_name='translations', to='voting.Voting')),
            ],
            options={
                'verbose_name': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434',
                'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b',
            },
        ),
        migrations.AddField(
            model_name='vote',
            name='voting',
            field=models.ForeignKey(to='voting.Voting'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='voting',
            field=models.ForeignKey(verbose_name='\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0443\u0447\u0430\u0441\u0442\u0432\u0443\u0435\u0442', to='voting.Voting'),
        ),
        migrations.AlterUniqueTogether(
            name='votingtranslation',
            unique_together=set([('parent', 'language_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('person', 'voting')]),
        ),
    ]
