# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_auto_20160822_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreVoting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('end_date', models.DateTimeField(null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u0440\u0435\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='PreVotingTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=7, verbose_name=b'\xd0\xaf\xd0\xb7\xd1\x8b\xd0\xba', choices=[(b'ru', 'Russian'), (b'en', 'English')])),
                ('description', redactor.fields.RedactorField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('parent', models.ForeignKey(related_name='translations', to='voting.PreVoting')),
            ],
            options={
                'verbose_name': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434',
                'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b',
            },
        ),
        migrations.AlterField(
            model_name='candidatetranslation',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='voting',
            name='prevoting',
            field=models.ForeignKey(verbose_name='\u041f\u0440\u0435\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435', blank=True, to='voting.PreVoting', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='prevotingtranslation',
            unique_together=set([('parent', 'language_code')]),
        ),
    ]
