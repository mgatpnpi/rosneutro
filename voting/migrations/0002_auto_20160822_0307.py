# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=7, verbose_name=b'\xd0\xaf\xd0\xb7\xd1\x8b\xd0\xba', choices=[(b'ru', 'Russian'), (b'en', 'English')])),
                ('description', redactor.fields.RedactorField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('parent', models.ForeignKey(related_name='translations', to='voting.Candidate')),
            ],
            options={
                'verbose_name': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434',
                'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b',
            },
        ),
        migrations.AlterUniqueTogether(
            name='candidatetranslation',
            unique_together=set([('parent', 'language_code')]),
        ),
    ]
