from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Room(Base):
  __tablename__ = "rooms"
  
  id = Column(Integer, primary_key=True, index=True)
  capacity = Column(Integer, nullable=False)
  roon_number = Column(String, nullable=False)
  occupied_bed = Column(Integer,nullable=False,default=0)
  pg_id = Column(Integer, ForeignKey("pgs.id"), nullable=False)
  pg =  relationship("PG",backref="rooms")