from fastapi import APIRouter, Depends, status
from blog import database, schemas, models
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=['User']
)

get_db = database.get_db

""" USER"""

@router.post('/', response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)