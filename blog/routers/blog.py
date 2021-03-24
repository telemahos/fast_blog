from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import blog, user

router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.Blog])
def all_blog(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session=Depends(get_db)):
    return blog.create(request, db)

#  
@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
def destroy_blog(id:int , db: Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id:int , request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_Blog(id: int, db: Session = Depends(get_db)):
    return blog.show(id, db)