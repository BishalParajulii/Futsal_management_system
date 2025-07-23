from pydantic import BaseModel

class FutsalCreate(BaseModel):
    name : str
    location : str
    price_per_hour : int
    
class FutsalOut(BaseModel):
    id : int
    
    class Config:
        orm_mode = True
        
        