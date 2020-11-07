FROM python:3.8-slim-buster

WORKDIR /usr/src/app

RUN addgroup --system app && adduser --system --no-create-home --group app

RUN apt-get update && apt-get install -y --no-install-recommends nginx gcc python3-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install uwsgi

COPY ./app.py /usr/src/app/
COPY ./docker_files/entrypoint.sh /usr/src/app/
COPY ./docker_files/uwsgi.ini /usr/src/app/
COPY ./docker_files/nginx.conf /etc/nginx/nginx.conf

RUN chmod +x /usr/src/app/entrypoint.sh
RUN chown -R app:app /usr/src/app && chmod -R 755 /usr/src/app

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /usr/src/app

EXPOSE 80

#USER app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]