FROM python:3.8.4-alpine

LABEL maintainer="Giuliano Di Pasquale <giuliano@dipasquale.dev>"

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

ENV PYTHONPATH=/app

EXPOSE 8000
ENTRYPOINT python3 /app/main.py
