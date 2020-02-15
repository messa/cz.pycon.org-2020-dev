FROM node:12 AS npm

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY pyconcz/static_src ./pyconcz/static_src
COPY gulpfile.js ./
RUN npm run build

FROM python:3.7-buster

ENV PYTHONUNBUFFERED=1 DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y --no-install-recommends libz-dev libjpeg-dev libtiff-dev libfreetype6-dev build-essential

WORKDIR /app

COPY 2015 ./2015
COPY 2016 ./2016
COPY 2017 ./2017
COPY 2018 ,/2018
#COPY 2019 ./2019
COPY 2020 ./2020

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY pyconcz ./pyconcz
COPY manage.py app.py docker_entrypoint.sh ./
COPY --from=npm /app/pyconcz/static ./pyconcz/static

ENV STATIC_ROOT=/app/static
RUN python manage.py collectstatic --no-input

RUN groupadd --gid 1100 app && useradd --system --gid 1100 --uid 1100 --shell /usr/sbin/nologin app

EXPOSE 8000
USER app:app
CMD ["bash", "docker_entrypoint.sh"]
