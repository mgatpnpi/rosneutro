# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20160311_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'\xd0\xa3\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd0\xb5\xd0\xbf\xd0\xb5\xd0\xbd\xd1\x8c', choices=[('\u043a.\u0444.-\u043c.\u043d.', '\u043a.\u0444.-\u043c.\u043d.'), ('\u0434.\u0444.-\u043c.\u043d.', '\u0434.\u0444.-\u043c.\u043d.'), ('\u043a.\u0442.\u043d.', '\u043a.\u0442.\u043d.'), ('\u0434.\u0442.\u043d.', '\u0434.\u0442.\u043d.'), ('\u043a.\u0431.\u043d.', '\u043a.\u0431.\u043d.'), ('\u0434.\u0431.\u043d.', '\u0434.\u0431.\u043d.'), ('\u043a.\u0445.\u043d.', '\u043a.\u0445.\u043d.'), ('\u0434.\u0445.\u043d.', '\u0434.\u0445.\u043d.'), ('\u043a.\u0433.-\u043c.\u043d.', '\u043a.\u0433.-\u043c.\u043d.'), ('\u0434.\u0433.-\u043c.\u043d.', '\u0434.\u0433.-\u043c.\u043d.'), ('\u043a.\u0438.\u043d.', '\u043a.\u0438.\u043d.'), ('\u0434.\u0438.\u043d.', '\u0434.\u0438.\u043d.'), ('\u043a.\u043c.\u043d.', '\u043a.\u043c.\u043d.'), ('\u0434.\u043c.\u043d.', '\u0434.\u043c.\u043d.'), ('\u043a.\u0444\u0430\u0440\u043c.\u043d.', '\u043a.\u0444\u0430\u0440\u043c.\u043d.'), ('\u0434.\u0444\u0430\u0440\u043c.\u043d.', '\u0434.\u0444\u0430\u0440\u043c.\u043d.')]),
        ),
    ]
