from pydantic import BaseModel
from enum import Enum
from app.database.database import Base

class UserRole(Enum):
  OWNER="OWNER"
  TENANT="TENANT"
  
class UserCreate(BaseModel):
  firstName: str
  lastName: str
  email: str
  phone: int
  role: UserRole
  password: str

class UserResponse(BaseModel):
  id: int
  name: str
  email: str
  