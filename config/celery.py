from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check_premium': {
        'task': 'apps.users.tasks.check_expired_premium',
        'schedule': crontab(minute='*/2')
       # 'schedule':  crontab(hour="3", minute="30", day_of_week="1"),  # время проверки

    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
