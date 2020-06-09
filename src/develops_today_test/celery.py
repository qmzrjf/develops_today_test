import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "develops_today_test.settings")
app = Celery("develops_today_test")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
