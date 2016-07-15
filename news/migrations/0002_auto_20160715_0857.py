# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsposttranslation',
            options={'verbose_name': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434', 'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b'},
        ),
    ]
