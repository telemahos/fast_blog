from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter()
get_db = database.get_db

@router.get('/blog', response_model=List[schemas.Blog], tags=['Blog'])
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blog'])
def create_blog(request: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, author_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
async def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    query = text("""UPDATE blogs SET title=:title, body=:body WHERE id = :id""").params(title=request.title, body=request.body, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The post with id {id} is not found')
    db.commit()
    return request


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
def destroy_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'The post with id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blog'])
def show_Blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Blog with ID {id} is not found')
    return blog