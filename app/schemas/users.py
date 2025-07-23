from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    email : str
    password : str
    user_type : str
    phone_number : int
    
class UserOut(BaseModel):
    id : int
    name : str
    email : str
    user_type : str
    phone_number : int
    
    class Config:
        orm_model = True