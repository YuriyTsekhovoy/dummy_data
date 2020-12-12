from celery import Celery

app = Celery('hello')

@app.task
def hello():
    return 'hello world'


@app.task
def add(x, y):
    return x + y