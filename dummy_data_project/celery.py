import celery
from fake_data.fake_factory import gen_fake_data
app = celery.Celery('dummy_data_project')


@app.task
def generate(*args, **kwargs):
    return gen_fake_data(*args, **kwargs)
