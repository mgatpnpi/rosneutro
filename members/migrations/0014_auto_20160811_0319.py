# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_secret_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomEmailMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d')),
                ('subject', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043c\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('message', models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('subscribers_only', models.BooleanField(default=True, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc')),
                ('attachment1', models.FileField(upload_to=b'emailing', null=True, verbose_name='\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b', blank=True)),
                ('attachment2', models.FileField(upload_to=b'emailing', null=True, verbose_name='\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b', blank=True)),
                ('attachment3', models.FileField(upload_to=b'emailing', null=True, verbose_name='\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b', blank=True)),
                ('send', models.BooleanField(default=False, verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c')),
                ('sent', models.DateTimeField(default=None, null=True, verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(max_length=255, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True),
        ),
    ]
