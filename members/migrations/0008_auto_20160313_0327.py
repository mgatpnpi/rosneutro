# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20160311_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='interests',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='\u041d\u0430\u0443\u0447\u043d\u044b\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u044b', choices=[(b'Biology', 'Biology'), (b'Chemistry', 'Chemistry'), (b'Crystallography', 'Crystallography'), (b'Engineering', 'Engineering'), (b'Cond. Matter Physics', 'Cond. Matter Physics'), (b'Fundamental Physics', 'Fundamental Physics'), (b'Ceramics', 'Ceramics'), (b'Metallic Materials', 'Metallic Materials'), (b'Polymers', 'Polymers'), (b'Other Materials Science', 'Other Materials Science'), (b'Instrumentation', 'Instrumentation'), (b'Other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u0430\u043d \u043d\u0430 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0443'),
        ),
    ]
