web: gunicorn dummy_data_project.wsgi --log-file -
worker: celery -A dummy_data_project.celery.app worker
