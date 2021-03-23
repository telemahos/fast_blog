from fastapi import FastAPI, Depends, status, Response, HTTPException, Request
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, SessionLocal
from typing import List
from . hash import Hash
import uvicorn
# On video 2:04

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
async def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    query = text("""UPDATE blogs SET title=:title, body=:body WHERE id = :id""").params(title=request.title, body=request.body, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The post with id {id} is not found')
    db.commit()
    return request

@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blog'])
def create_blog(request: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
def destroy_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'The post with id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blog'])
def show_Blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Blog with ID {id} is not found')
    return blog

@app.get('/blog', response_model=List[schemas.Blog], tags=['Blog'])
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


""" USER"""



@app.post('/user', response_model=schemas.ShowUser, tags=['User'])
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with ID {id} is not found')
    return user