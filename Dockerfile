FROM python:3.11.4-alpine

COPY . /app

ARG main.py .

WORKDIR /app

CMD [ "python", "main.py" ]