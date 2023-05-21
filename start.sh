#!/bin/sh

cd /opt/app && gunicorn --bind=0.0.0.0:5000 --log-level=warning app:app --daemon
nginx -g "daemon off;"