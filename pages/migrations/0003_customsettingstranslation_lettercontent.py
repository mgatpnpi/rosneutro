# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_customsettingstranslation_formpagecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customsettingstranslation',
            name='lettercontent',
            field=redactor.fields.RedactorField(null=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\x92\xd0\xb0\xd1\x85\xd1\x80\xd1\x83\xd1\x88\xd0\xb5\xd0\xb2\xd0\xb0', blank=True),
        ),
    ]
