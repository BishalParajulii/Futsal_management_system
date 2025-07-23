from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserOut
from app.crud import users as user_crud
from app.db.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/register", response_model=UserOut)
def register(user : UserCreate , db : Session = Depends(get_db)):
    return user_crud.create_user(db, user)
