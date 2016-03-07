# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb4\xd0\xb8\xd0\xbb Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'\xd0\xa3\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd0\xb5\xd0\xbf\xd0\xb5\xd0\xbd\xd1\x8c', choices=[(b'prof', b'\xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb5\xd1\x81\xd1\x81\xd0\xbe\xd1\x80'), (b'doc', b'\xd0\xb4\xd0\xbe\xd0\xba\xd1\x82\xd0\xbe\xd1\x80'), (b'cand', b'\xd0\xba\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb8\xd0\xb4\xd0\xb0\xd1\x82')]),
        ),
    ]
