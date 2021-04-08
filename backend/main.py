from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authendication
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Deta
# Project Key: a07rzxne_PYUWRDdTuQBKZka9h5Y9UNDFcZC3Qvah
# Project ID: a07rzxne

# On video 3:30
# TODO
# repository/delete problem

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authendication.router)
app.include_router(blog.router)
app.include_router(user.router)

# app.router.redirect_slashes = False

origins = ["*"]
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:8000",
#     "http://localhost:5500/frontend/",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


