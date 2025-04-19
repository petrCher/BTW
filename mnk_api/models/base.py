from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import find_dotenv, load_dotenv, dotenv_values



# --------------------------
# enable cors, or cross origin request something
# allows frontend to talk to backend
#
# app = FastAPI()

# address of frontend server in quotes
origins = [
    "http://frontend:8080",
]



# load_dotenv(find_dotenv(".env"))
# config = dotenv_values()

# engine = create_engine(config["DB_DSN"])
engine = create_engine("postgresql://postgres@localhost:5433")
db_session: Session = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    try:
        with db_session() as session:
            yield session
    finally:
        session.close()

