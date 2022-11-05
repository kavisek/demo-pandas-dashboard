# POETRY COMMANDS

.PHONY: install
pinstall:
	poetry install

.PHONY: build
pbuild: install
	poetry build

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --without-hashes -o requirements.txt

.PHONY: black
black:
	poetry run black .

.PHONY: pytest
pytest:
	poetry run pytest --cov=./tests --black -rAP 

.PHONY:black
black:
	isort

# FAST API COMMANDS

puvicorn:
	poetry run uvicorn --port 8080 --host 0.0.0.0 main:app --reload