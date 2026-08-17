from fastapi import APIRouter,Depends,HTTPException, status
from app.database.database import get_db
from app.crud.user import create_user,get_user,get_user_by_email,get_user_by_id
from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.schemas.user import UserCreate,UserResponse,UserLogin

router = APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=201)
def register(user:UserCreate,db: Session = Depends(get_db)):
  existing_user = get_user_by_email(user.email)
  if existing_user:
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
  return create_user(db,user)

@router.post("/login",response_model=UserResponse,status_code=201)
def login(user:UserLogin,db:Session = Depends(get_db)):
  db_user = get_user
  existing_user = get_user_by_email(user.email)
  if not existing_user:
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
  if not verify_password(user.password, db_user.password):
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Invalid email or password"
      )
  return {
    "message":
      "Login successful",
      "user":
        {
          "name": existing_user.full_name,
          "email": existing_user.email,
          "role": existing_user.role
        }
  }


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id_route(user_id: int, db: Session = Depends(get_db)):
    """
    Example of path parameter.
    URL example: /auth/users/5
    """
    db_user = get_user_by_id(db, user_id)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    
    return db_user
# @router.get("/user",response_model=UserLogin)
  
@router.get("/users", response_model=UserResponse)
def get_user_by_email_route(email: str, db: Session = Depends(get_db)):
    """
    Example of query parameter.
    URL example: /auth/users?email=john@example.com
    """
    db_user = get_user_by_email(db, email)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return db_user