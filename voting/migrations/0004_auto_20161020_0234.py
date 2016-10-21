# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20161019_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='agree',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='candidatetranslation',
            name='language_code',
            field=models.CharField(max_length=7, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', 'Russian'), (b'en', 'English')]),
        ),
        migrations.AlterField(
            model_name='prevoting',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='prevoting',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e'),
        ),
        migrations.AlterField(
            model_name='prevotingtranslation',
            name='language_code',
            field=models.CharField(max_length=7, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', 'Russian'), (b'en', 'English')]),
        ),
        migrations.AlterField(
            model_name='voting',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e'),
        ),
        migrations.AlterField(
            model_name='votingtranslation',
            name='language_code',
            field=models.CharField(max_length=7, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', 'Russian'), (b'en', 'English')]),
        ),
    ]
