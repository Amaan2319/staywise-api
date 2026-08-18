from pydantic import BaseModel,ConfigDict
from enum import Enum
from app.database.database import Base

class UserRole(str,Enum):
  OWNER="OWNER"
  TENANT="TENANT"
  
class UserCreate(BaseModel):
  full_name: str
  email: str
  phone: str
  role: UserRole
  password: str

class UserLogin(BaseModel):
  email: str
  password: str

class UserResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  full_name: str
  email: str
  phone: str
  role: UserRole
  
class TokenResponse(BaseModel):
  access_token: str
  token_type: str