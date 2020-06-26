FROM python:3.7

RUN mkdir app
WORKDIR /app

ENV TELEGRAM_API_TOKEN="1198378294:AAFtfjhe1iU-R79-VCj04a-PRPySOmOW6Bc"

RUN pip install -U pip aiogram requests && apt-get update
COPY *.py /app/

ENTRYPOINT ["python", "app.py"]