from sqlalchemy.orm import Session

from app.models.user import User as DBUser
from app.schemas.user import UserCreate,UserLogin
from app.core.security import hash_password


def create_user(db: Session, user: UserCreate):

    db_user = DBUser(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        role=user.role,
        password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user(db:Session,email:str):
    db_user = db.query(DBUser).filter(email==DBUser.email)
    return db_user

def get_user_by_email(db:Session,email:str):
    db_user = db.query(DBUser).filter(email==email).limit(1)