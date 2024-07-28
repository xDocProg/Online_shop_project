import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')

app = Celery('shop_project', broker_connection_retry=False,
             broker_connection_retry_on_startup=True)

app.config_from_object('django.conf:settings', namespace='CELERY')
broker_connection_retry = False

app.autodiscover_tasks()

