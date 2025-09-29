import os
import time

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imageproject.settings')

app = Celery('imageproject')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

