from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import Contact
from mysite.database.schema import ContactInputSchema, ContactOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

contact_router = APIRouter(prefix='/contact', tags=['Contact'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contact_router.post('/', response_model=ContactOutSchema)
async def create_contact(contact: ContactInputSchema, db: Session = Depends(get_db)):
    contact_db = Contact(**contact.dict())
    db.add(contact_db)
    db.commit()
    db.refresh(contact_db)
    return contact_db


@contact_router.get('/', response_model=List[ContactOutSchema])
async def list_contact(db: Session = Depends(get_db)):
    return db.query(Contact).all()


@contact_router.get('/{contact_id}/', response_model=ContactOutSchema)
async def detail_contact(contact_id: int, db: Session = Depends(get_db)):
    contact_db = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact_db:
        raise HTTPException(detail='Contact не найден', status_code=400)
    return contact_db


@contact_router.put('/{contact_id}/', response_model=dict)
async def update_contact(contact_id: int, contact: ContactInputSchema,
                         db: Session = Depends(get_db)):
    contact_db = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact_db:
        raise HTTPException(detail='Contact не найден', status_code=400)

    for key, value in contact.dict().items():
        setattr(contact_db, key, value)

    db.commit()
    db.refresh(contact_db)
    return {'message': 'Contact успешно обновлен'}


@contact_router.delete('/{contact_id}/', response_model=dict)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact_db = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact_db:
        raise HTTPException(detail='Contact не найден', status_code=400)

    db.delete(contact_db)
    db.commit()
    return {'message': 'Contact удален'}