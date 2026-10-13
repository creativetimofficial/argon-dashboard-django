# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

# Cloud Run sets the PORT environment variable
port = os.environ.get('PORT', '8080')
bind = f'0.0.0.0:{port}'

# Recommended workers: 2-4 x $(NUM_CORES)
workers = int(os.environ.get('GUNICORN_WORKERS', '2'))
threads = int(os.environ.get('GUNICORN_THREADS', '4'))
worker_class = 'gthread'

accesslog = '-'
errorlog = '-'
loglevel = os.environ.get('LOG_LEVEL', 'info')
capture_output = True
enable_stdio_inheritance = True

# Timeout settings
timeout = 120
keepalive = 5
