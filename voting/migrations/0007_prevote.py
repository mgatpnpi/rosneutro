# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_auto_20161020_0234'),
        ('voting', '0006_auto_20161020_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remarks', models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u0436\u0435\u043b\u0430\u043d\u0438\u044f', blank=True)),
                ('candidates', models.ManyToManyField(to='members.Person', null=True, verbose_name='\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u043e\u0432', blank=True)),
                ('prevoting', models.ForeignKey(verbose_name='\u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435', blank=True, to='voting.PreVoting', null=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0433\u043e\u043b\u043e\u0441',
                'verbose_name_plural': '\u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0433\u043e\u043b\u043e\u0441\u0430',
            },
        ),
    ]
