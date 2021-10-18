FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /code
WORKDIR /code

COPY . /code
RUN python -m pip install -r requirements.txt

CMD python manage.py runserver