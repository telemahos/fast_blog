from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authendication
import uvicorn


# On video 3:53
# TODO
# repository/delete problem

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authendication.router)
app.include_router(blog.router)
app.include_router(user.router)


