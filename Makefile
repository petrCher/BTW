run:
	source ./venv/bin/activate && uvicorn --reload --log-config logging_dev.conf mnk_api.routes.base:app

configure: venv
	source ./venv/bin/activate && pip install -r requirements.dev.txt -r requirements.txt

venv:
	python3.11 -m venv venv

format:
	autoflake -r --in-place --remove-all-unused-imports ./mnk_api
	isort ./mnk_api
	black ./mnk_api
	autoflake -r --in-place --remove-all-unused-imports ./migrations
	isort ./migrations
	black ./migrations
	
db:
	docker run -d -p 5433:5432 -e POSTGRES_HOST_AUTH_METHOD=trust --name db-mnk_api postgres:15

migrate:
	alembic upgrade head
