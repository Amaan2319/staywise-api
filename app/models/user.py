from enum import Enum
from sqlalchemy import Column,Integer,String,Enum as SqlEnum
from app.database.database import Base
from app.schemas.user import UserRole



class User(Base):
  __tablename__ = 'users'
  
  id=Column(Integer,primary_key=True,index=True)
  full_name=Column(String,nullable=False)
  email=Column(String,nullable=False)
  password = Column(String, nullable=False)

  phone = Column(String, nullable=False)

  role = Column(SqlEnum(UserRole), nullable=False)