# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_auto_20160811_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customemailmessage',
            name='send',
        ),
    ]
