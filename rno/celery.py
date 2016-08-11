from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rno.settings')

from django.conf import settings  # noqa

app = Celery('rno')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.control.rate_limit('rno.send_email_message', '100/h')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
