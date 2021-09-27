FROM python:3.9.0

WORKDIR /home/

RUN echo 'agehewa'

RUN git clone https://github.com/chogoal/Web1.git

WORKDIR /home/Web1/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=project01.settings.deploy && python manage.py migrate --settings=project01.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=project01.settings.deploy project01.wsgi --bind 0.0.0.0:8000"]
