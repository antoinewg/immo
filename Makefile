install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

lint:
	black .

test:
	python -m pytest

serve:
	python manage.py runserver 127.0.0.1:8001