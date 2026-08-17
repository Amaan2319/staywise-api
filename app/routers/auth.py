from fastapi import APIRouter,Depends
from app.database.database import get_db
from app.crud.user import create_user,get_user,get_user_by_email
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate,UserResponse,UserLogin

router = APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=201)
def register(user:UserCreate,db: Session = Depends(get_db)):
  existing_user = get_user_by_email(user.email)
  if existing_user:
    return {"message": "User already exists"}
  return create_user(db,user)

@router.get("/login",response_model=UserResponse,status_code=201)
def login(user:UserLogin,db:Session = Depends(get_db)):
  db_user = get_user
  return {"message": f"User logged in sucessfully {db_user}"}


@router.get("/user/id",response_model=UserLogin,status_code=201)
def getUser(email:str,deb:Session=Depends(get_db)):
   db_user = get_user(email)
   return db_user
# @router.get("/user",response_model=UserLogin)
  