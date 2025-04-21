run:
	source ./venv/bin/activate && uvicorn --reload --log-config logging_dev.conf mnk_api.__main__:app
configure: venv
	source ./venv/bin/activate && python3 -m pip install -r requirements.dev.txt -r requirements.txt --force-reinstall

venv:
	python3.11 -m venv venv

db:
	docker run -d -p 5433:5432 -e POSTGRES_HOST_AUTH_METHOD=trust --name db-mnk_api postgres:15

migrate:
	alembic revision --autogenerate -m "init" && alembic upgrade head

full_configure:
	configure
	db
	migrate
	run
