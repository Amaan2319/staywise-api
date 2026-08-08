from fastapi import APIRouter,Depends
from app.database.database import get_db
from app.crud.user import create_user,get_user
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate,UserResponse,UserLogin

router = APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=201)
def register(user:UserCreate,db: Session = Depends(get_db)):
  return create_user(db,user)

@router.get("/login",response_model=UserResponse,status_code=201)
def login(user:UserLogin,db:Session = Depends(get_db)):
  db_user = get_user
  return {"message": f"User logged in sucessfully {db_user}"}


@router.get("/user/id",response_model=UserLogin,status_code=201)
def getUser(user:UserLogin,deb:Session=Depends(get_db)):
    return {"message": "user fetched"}
# @router.get("/user",response_model=UserLogin)
  