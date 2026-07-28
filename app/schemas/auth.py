from pydantic import BaseModel, EmailStr, Field
class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    phone_number: str | None = Field(None, min_length=10, max_length=15)
    
    
class UserLogin(BaseModel):
        email: EmailStr
        password: str 
        
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: str | None
    role: str
    is_active: bool
    is_verified: bool

    class Config: {
        "from_attributes" : True
    } 