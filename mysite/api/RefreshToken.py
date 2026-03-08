from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import RefreshToken
from mysite.database.schema import RefreshTokenInputSchema, RefreshTokenOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

refresh_token_router = APIRouter(prefix='/refresh-token', tags=['RefreshToken'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@refresh_token_router.post('/', response_model=RefreshTokenOutSchema)
async def create_refresh_token(token: RefreshTokenInputSchema, db: Session = Depends(get_db)):
    token_db = RefreshToken(**token.dict())
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return token_db


@refresh_token_router.get('/', response_model=List[RefreshTokenOutSchema])
async def list_refresh_token(db: Session = Depends(get_db)):
    return db.query(RefreshToken).all()


@refresh_token_router.get('/{token_id}/', response_model=RefreshTokenOutSchema)
async def detail_refresh_token(token_id: int, db: Session = Depends(get_db)):
    token_db = db.query(RefreshToken).filter(RefreshToken.id == token_id).first()
    if not token_db:
        raise HTTPException(detail='RefreshToken не найден', status_code=400)
    return token_db


@refresh_token_router.put('/{token_id}/', response_model=dict)
async def update_refresh_token(token_id: int, token: RefreshTokenInputSchema,
                               db: Session = Depends(get_db)):
    token_db = db.query(RefreshToken).filter(RefreshToken.id == token_id).first()
    if not token_db:
        raise HTTPException(detail='RefreshToken не найден', status_code=400)

    for key, value in token.dict().items():
        setattr(token_db, key, value)

    db.commit()
    db.refresh(token_db)
    return {'message': 'RefreshToken успешно обновлен'}


@refresh_token_router.delete('/{token_id}/', response_model=dict)
async def delete_refresh_token(token_id: int, db: Session = Depends(get_db)):
    token_db = db.query(RefreshToken).filter(RefreshToken.id == token_id).first()
    if not token_db:
        raise HTTPException(detail='RefreshToken не найден', status_code=400)

    db.delete(token_db)
    db.commit()
    return {'message': 'RefreshToken удален'}