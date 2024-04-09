import os

bind = '0.0.0.0:8000'
workers = int(os.environ.get('GUNICORN_WORKERS', 1))
worker_tmp_dir = '/dev/shm'
chdir = 'blogpost'
max_requests = int(os.environ.get('GUNICORN_MAX_REQUESTS', '1000'))
max_requests_jitter = int(os.environ.get('GUNICORN_MAX_REQUESTS_JITTER', '25'))
graceful_timeout = 30