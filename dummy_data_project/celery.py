import celery
from fake_data.fake_factory import gen_fake_data
app = celery.Celery('dummy_data_project')

@app.task
def add(x, y):
    return x + y

@app.task
def generate():
    return gen_fake_data(20)