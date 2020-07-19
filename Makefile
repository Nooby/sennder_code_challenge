
build:
	docker-compose build

start:
	docker-compose up -d

lint:
	flake8 --exclude=test_*.py */*.py

test:
	coverage run --source=app -m unittest discover
	coverage report
