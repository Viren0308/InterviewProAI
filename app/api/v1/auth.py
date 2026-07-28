from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import UserRegister, UserResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth", 
    tags=["Authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    try:
        new_user = AuthService.register_user(db, user)
        
        
        return {
            "message": "User registered successfully", 
            "user": new_user.id}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))