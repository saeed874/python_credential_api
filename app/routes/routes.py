

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.model.user import User

from app.schemas.schemas import UserCreate, UserOut

from app.utils.auth import hash_password



router = APIRouter()


@router.post("/users", response_model=UserOut)

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user =db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(**user.dict())
    hashed_pw = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=hashed_pw
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()



