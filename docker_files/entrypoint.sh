#!/bin/bash
set -m

uwsgi --ini /usr/src/app/uwsgi.ini && nginx -g "pid /tmp/nginx.pid;" -c /etc/nginx/nginx.conf