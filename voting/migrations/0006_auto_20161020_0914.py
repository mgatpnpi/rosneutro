# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_auto_20161020_0234'),
        ('voting', '0005_auto_20161020_0253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prevoting',
            options={'verbose_name': '\u041f\u0440\u0435\u0434\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435', 'verbose_name_plural': '\u041f\u0440\u0435\u0434\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f'},
        ),
        migrations.AddField(
            model_name='prevoting',
            name='prevoters',
            field=models.ManyToManyField(related_name='prevotings', null=True, verbose_name='\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0432\u0448\u0438\u0435 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432', to='members.Person', blank=True),
        ),
        migrations.AddField(
            model_name='prevoting',
            name='proposed_candidates',
            field=models.ManyToManyField(to='members.Person', null=True, verbose_name='\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='voting',
            name='voters',
            field=models.ManyToManyField(related_name='votings', null=True, verbose_name='\u041f\u0440\u043e\u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u0432\u0448\u0438\u0435', to='members.Person', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='candidate',
            unique_together=set([('person', 'voting')]),
        ),
    ]
