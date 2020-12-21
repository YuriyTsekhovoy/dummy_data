import celery
import environ

from fake_data.fake_factory import gen_fake_data
from django.conf import settings


env = environ.Env()
app = celery.Celery('dummy_data_project')

app.conf.update(BROKER_URL=env('REDIS_URL'),
                CELERY_RESULT_BACKEND=env('REDIS_URL'))
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def generate(*args, **kwargs):
    return gen_fake_data(*args, **kwargs)
