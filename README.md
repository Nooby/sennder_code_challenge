# Sennder Code Challenge

This is my solution to the Sennder GmbH Backend Code Challenge. The goal of this challege is to create a Python application which serves a page on localhost:8000/movies/ listing all Movies and Charakters of the Studio Ghibli movies. The data for this application should be queried from https://ghibliapi.herokuapp.com/ and this API should not be queried on each request. Furthermore the information displayed on the page should not be older then 1 minute.

## Requirements

- Docker (19.03+)
- Docker-Compose
- Make (optional)

## Build and Run

```bash
# To build the docker image run the following command
make build
# To start the project using docker-compose run the following command
make start
```

## Testing

To run the unittests simply install the python requirements in `requirements_dev.txt` then call `make test`.  The use of a virtualenvironment is recommended. Running the unittests via `make test` will also produce a short coverage report. A detailed report can be generated via `coverage html`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_dev.txt
make test
```

Currently the Unittests are only rudamentary and can be improved by adding Tests for edge and error cases. The tests can then be further improved by unittesting the Flask View function and by adding integration tests.
