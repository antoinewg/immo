install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

lint:
	black .

test:
	python -m pytest