from sqlalchemy.orm import Session


from app.models.user import User
from app.schemas.auth import UserRegister
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password

class AuthService:
    
    @staticmethod
    def register_user(db: Session, user_data: UserRegister):
        
        existing_user = UserRepository.get_user_by_email(
            db, 
            user_data.email
        )
        
        if existing_user:
            raise ValueError("User with this email already exists.")
        exitsting_phone_user = UserRepository.get_by_phone(
            db,
            user_data.phone_number
        )
        if exitsting_phone_user:
            raise ValueError("User with this phone number already exists.")

        new_user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            phone_number=user_data.phone_number,
            password_hash=hash_password(user_data.password)
        )
        
        return UserRepository.create(db, new_user)