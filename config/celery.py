# config/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Загружаем конфиг из django.conf:settings (если нужны настройки CELERY_...)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автопоиск tasks.py
app.autodiscover_tasks()

# Теперь можно настраивать beat_schedule
app.conf.beat_schedule = {
    'check_premium': {
        'task': 'users.tasks.check_expired_premium',
        'schedule': crontab(minute=0, hour='*'),  # каждый час
        # 'args': ()  # если нужны аргументы
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
