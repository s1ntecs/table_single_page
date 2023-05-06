FROM python:3.10-slim
LABEL owner="sintecs@list.com"

RUN mkdir /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY djhtmxfun/ /app

WORKDIR /app

CMD ["gunicorn", "djhtmxfun.wsgi:application", "--bind", "0:8000" ]