FROM python:3

WORKDIR /django_todo
COPY . .

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

ENTRYPOINT ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_todo.asgi:application"]
