# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0011_create_users_for_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d')),
                ('secret', models.SlugField(verbose_name='\u0421\u0435\u043a\u0440\u0435\u0442')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': '\u0421\u0435\u043a\u0440\u0435\u0442 \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430',
                'verbose_name_plural': '\u0421\u0435\u043a\u0440\u0435\u0442\u044b \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430',
            },
        ),
    ]
