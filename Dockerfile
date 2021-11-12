FROM python:3.9

ENV PYTHONPATH=/app
# ENV DJANGO_SETTINGS_MODULE=gooey.settings

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# RUN rm db.sqlite3
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "manage.py runserver"]