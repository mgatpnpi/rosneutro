# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160715_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposttranslation',
            name='language_code',
            field=models.CharField(max_length=7, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', 'Russian'), (b'en', 'English')]),
        ),
    ]
