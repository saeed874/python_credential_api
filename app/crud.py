from app.model.user import User

from app.database import SessionLocal

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def create_user(user):
    db = SessionLocal()
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user
