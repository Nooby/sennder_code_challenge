
build:
	docker-compose build

start:
	docker-compose up -d

lint:
	flake8 */*.py
