FROM python:latest

COPY app.py .

WORKDIR /client/

CMD [ "python", "app.py"]