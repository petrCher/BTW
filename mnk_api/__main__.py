from fastapi import FastAPI
import uvicorn
from mnk_api.routes.profile import profile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Физические практикумы", description="Познакомьтесь с интересными людьми")

app.include_router(profile)

# --------------------------
# enable cors, or cross origin request something
# allows frontend to talk to backend
#
# app = FastAPI()

# address of frontend server in quotes
origins = [
    "http://frontend:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------

# i specified 0.0.0.0 because apparently 127.0.0.1 cannot be reached outside of the docker container
# update: nah it miraculously worked, dont know why lol
if __name__ == "__main__":
    # uvicorn.run(app, port=8000)
    uvicorn.run(app, port=8000, host='0.0.0.0')
