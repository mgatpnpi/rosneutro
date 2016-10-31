# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_auto_20160816_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customemailmessage',
            name='subscribers_only',
            field=models.BooleanField(default=True, verbose_name='\u0422\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u043c'),
        ),
    ]
