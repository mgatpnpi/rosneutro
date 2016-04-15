# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20160313_0327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name', 'middle_name'), 'verbose_name': '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a', 'verbose_name_plural': '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0438'},
        ),
    ]
