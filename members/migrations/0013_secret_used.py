# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='used',
            field=models.BooleanField(default=False, verbose_name='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d'),
        ),
    ]
