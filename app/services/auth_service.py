from sqlalchemy.orm import session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password

class AuthService:
    
    @staticmethod
    def register_user(db: session, user_data):
        
        existing_user = UserRepository.get_user_by_email(
            db, 
            user_data.email
        )
        
        if existing_user:
            raise ValueError("User with this email already exists.")
        
        new_user = User(          
            full_name=user_data.full_name,
            email=user_data.email,
            password=hash_password(user_data.password)
        )
        
        return UserRepository.create_user(db, new_user)