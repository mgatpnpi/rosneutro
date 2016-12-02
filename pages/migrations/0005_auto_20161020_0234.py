# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_customsettingstranslation_requestsessioncontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsettingstranslation',
            name='formpagecontent',
            field=redactor.fields.RedactorField(null=True, verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0441 \u0444\u043e\u0440\u043c\u043e\u0439 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='customsettingstranslation',
            name='language_code',
            field=models.CharField(max_length=7, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', 'Russian'), (b'en', 'English')]),
        ),
        migrations.AlterField(
            model_name='customsettingstranslation',
            name='lettercontent',
            field=redactor.fields.RedactorField(null=True, verbose_name='\u041e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u0412\u0430\u0445\u0440\u0443\u0448\u0435\u0432\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='customsettingstranslation',
            name='mainpagecontent',
            field=redactor.fields.RedactorField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
        migrations.AlterField(
            model_name='customsettingstranslation',
            name='requestsessioncontent',
            field=redactor.fields.RedactorField(null=True, verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0441 \u0444\u043e\u0440\u043c\u043e\u0439 \u0437\u0430\u043f\u0440\u043e\u0441\u0430 \u0441\u0441\u044b\u043b\u043a\u0438 \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430', blank=True),
        ),
    ]
