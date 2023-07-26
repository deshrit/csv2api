# gunicorn configuration

bind = "0.0.0.0:8000"
accesslog = "-"
errorlog = "-"
workers = 3
threads = 3
wsgi_app = "core.wsgi:application"
