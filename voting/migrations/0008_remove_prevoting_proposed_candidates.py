# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_prevote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prevoting',
            name='proposed_candidates',
        ),
    ]
