#! /bin/sh
alembic revision --autogenerate
alembic upgrade head
exec "$@"
