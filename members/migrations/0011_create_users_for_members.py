# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def create_users_for_members(apps, schema_editor):
    Person = apps.get_model('members', 'Person')
    for person in Person.objects.all():
        person.save()

class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_person_user'),
    ]

    operations = [
            migrations.RunPython(create_users_for_members),
    ]
