# uvicorn app.main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import post, user, auth, votes
from .config import settings

# models.Base.metadata.create_all(bind=engine)
# before alembic, this was needed for SQLalchemy to create any tables that were missing

app = FastAPI()

origins = [
    "*"
]  # currently set as a wildcard i.e. everyone can send requests to our api...
# e.g. if we only wanted google, we could include "https://www.google.com"

app.add_middleware(
    CORSMiddleware,  # middleware is a function that runs before every request
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
