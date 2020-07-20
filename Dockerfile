FROM python:3.8.4-alpine

LABEL maintainer="Giuliano Di Pasquale <giuliano@dipasquale.dev>"

ENV PYTHONPATH=/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /src/app
COPY run.py /src

EXPOSE 8000
ENTRYPOINT python3 /src/run.py
