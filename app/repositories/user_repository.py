from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy.exc import SQLAlchemyError


class UserRepository:
    
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_by_phone(db: Session, phone_number: str):
        return db.query(User).filter(User.phone_number == phone_number).first()
    
    @staticmethod
    def create(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def create(db: Session, user: User):
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except SQLAlchemyError :
            db.rollback()
            raise 