# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_auto_20161020_0234'),
        ('voting', '0004_auto_20161020_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='voters',
            field=models.ManyToManyField(related_name='votings', verbose_name='\u041f\u0440\u043e\u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u0432\u0448\u0438\u0435', to='members.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='person',
        ),
    ]
