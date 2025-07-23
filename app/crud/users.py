from sqlalchemy.orm import Session
from app import schemas, db
from app.db import models
from app.core.security import get_password_hash
from app.schemas import users



def create_user(db : Session , user : users.UserCreate):
    hashed_psw = get_password_hash(user.password)
    db_user = models.User(
        name = user.name,
        email = user.email,
        hashed_password = hashed_psw,
        user_type = user.user_type,
        phone_number = user.phone_number
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def get_user_by_email(db : Session , email : str):
    return db.query(models.User).filter(models.User.email == email).first()