from fastapi import APIRouter,Depends
from app.database.database import get_db
from app.crud.user import create_user
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate,UserResponse

router = APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=201)
def register(user:UserCreate,db: Session = Depends(get_db)):
  return create_user(db,user)
  