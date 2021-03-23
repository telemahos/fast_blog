from fastapi import FastAPI
from sqlalchemy.sql import text
from . import models
from .database import engine
from .routers import blog, user
import uvicorn
# On video 3:01

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)

