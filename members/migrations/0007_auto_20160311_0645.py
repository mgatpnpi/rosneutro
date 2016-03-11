# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_person_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043do \u043f\u0440\u0430\u0432\u043e \u0433\u043e\u043b\u043e\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(help_text='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \u0434\u0434.\u043c\u043c.\u0433\u0433\u0433\u0433 \u0438\u043b\u0438 \u0433\u0433\u0433\u0433-\u043c\u043c-\u0434\u0434', verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u0423\u0447\u0435\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c', choices=[('\u043a.\u0444.-\u043c.\u043d.', '\u043a.\u0444.-\u043c.\u043d.'), ('\u0434.\u0444.-\u043c.\u043d.', '\u0434.\u0444.-\u043c.\u043d.'), ('\u043a.\u0442.\u043d.', '\u043a.\u0442.\u043d.'), ('\u0434.\u0442.\u043d.', '\u0434.\u0442.\u043d.'), ('\u043a.\u0431.\u043d.', '\u043a.\u0431.\u043d.'), ('\u0434.\u0431.\u043d.', '\u0434.\u0431.\u043d.'), ('\u043a.\u0445.\u043d.', '\u043a.\u0445.\u043d.'), ('\u0434.\u0445.\u043d.', '\u0434.\u0445.\u043d.'), ('\u043a.\u0433.-\u043c.\u043d.', '\u043a.\u0433.-\u043c.\u043d.'), ('\u0434.\u0433.-\u043c.\u043d.', '\u0434.\u0433.-\u043c.\u043d.'), ('\u043a.\u0438.\u043d.', '\u043a.\u0438.\u043d.'), ('\u0434.\u0438.\u043d.', '\u0434.\u0438.\u043d.'), ('\u043a.\u043c.\u043d.', '\u043a.\u043c.\u043d.'), ('\u0434.\u043c.\u043d.', '\u0434.\u043c.\u043d.'), ('\u043a.\u0444\u0430\u0440\u043c.\u043d.', '\u043a.\u0444\u0430\u0440\u043c.\u043d.'), ('\u0434.\u0444\u0430\u0440\u043c.\u043d.', '\u0434.\u0444\u0430\u0440\u043c.\u043d.')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='interests',
            field=models.CharField(max_length=155, verbose_name='\u041d\u0430\u0443\u0447\u043d\u044b\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(max_length=255, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='person',
            name='note',
            field=models.TextField(null=True, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='organization',
            field=models.CharField(max_length=255, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(max_length=255, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='person',
            name='publications',
            field=models.TextField(help_text='\u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u0440\u043e\u0441\u0442\u043e \u0434\u0430\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0441\u0432\u043e\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c \u0432 Research Gate, \u0438\u043b\u0438 \u043d\u0430 \u0430\u043d\u0430\u043b\u043e\u0433\u0438\u0447\u043d\u044b\u0439 \u0440\u0435\u0441\u0443\u0440\u0441', verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='published',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d'),
        ),
        migrations.AlterField(
            model_name='person',
            name='random_string',
            field=models.SlugField(verbose_name='\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='person',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b Email'),
        ),
    ]
