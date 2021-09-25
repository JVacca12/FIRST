migrate:
	docker-compose exec web ./manage.py makemigrations
	docker-compose exec web ./manage.py migrate

requirements:
	docker-compose exec web pip install -r requirements.txt

statics:
	docker-compose exec web ./manage.py collectstatic --no-input

superuser:
	docker-compose exec web ./manage.py createsuperuser

app:
	docker-compose exec web ./manage.py startapp $(APP_NAME)