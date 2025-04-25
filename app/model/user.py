from sqlalchemy import Column, Integer, String
from app.database import Base , engine, get_db

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    password = Column(String, nullable=False)
    
