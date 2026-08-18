from fastapi import APIRouter,Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from app.database.database import get_db
from app.crud.user import create_user,get_user,get_user_by_email,get_user_by_id
from sqlalchemy.orm import Session
import jwt
from app.core.security import settings
from app.core.security import verify_password,create_access_token
from app.schemas.user import UserCreate,UserResponse,UserLogin,TokenResponse

router = APIRouter(prefix="/auth",tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token") 
@router.post("/register",response_model=UserResponse,status_code=201)
def register(user:UserCreate,db: Session = Depends(get_db)):
  existing_user = get_user_by_email(db,user.email)
  if existing_user:
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
  return create_user(db,user)

@router.post("/login",response_model=TokenResponse)
def login(user:UserLogin,db:Session = Depends(get_db)):
  existing_user = get_user_by_email(db,email=user.email)
  if not existing_user:
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
  if not verify_password(user.password, existing_user.password):
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Invalid email or password"
      )
  access_token = create_access_token(
        data={
            "sub": str(existing_user.id)
        }
    )
  return {
        "access_token": access_token,
        "token_type": "bearer"
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

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        user_id = int(user_id)

    except (jwt.InvalidTokenError, ValueError):
        raise credentials_exception

    user = get_user_by_id(db, user_id)

    if user is None:
        raise credentials_exception

    return 

@router.get("/me", response_model=UserResponse)
def get_current_user_route(
    current_user = Depends(get_current_user)
):
    return current_user

@router.post("/token", response_model=TokenResponse)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_email(
        db,
        email=form_data.username
    )

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password(
        form_data.password,
        existing_user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={
            "sub": str(existing_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }