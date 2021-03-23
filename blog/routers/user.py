from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hash import Hash

router = APIRouter()
get_db = database.get_db

""" USER"""

@router.post('/user', response_model=schemas.ShowUser, tags=['User'])
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with ID {id} is not found')
    return user