FROM python
WORKDIR /backend
# copying requirements.txt first is supposed to use caches and shit
# anyways i think it does build the image faster unless requirements.txt changes?
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# TODO: migrate the database here somehow?
# RUN alembic upgrade head && alembic revision --autogenerate

EXPOSE 8000

# # so apparently docker compose network is not created at the moment of running this dockerfile
# # im not sure how using entrypoint (what even is that lol) solves it but lets try
COPY entrypoint.sh .
ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD ["python3", "main.py"]
