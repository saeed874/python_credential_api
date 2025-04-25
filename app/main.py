from fastapi import FastAPI
from app import  crud
from app.database import Base, engine
from app.routes import routes

from app.model.user import User

from app.routes import auth  




Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routes.router)
app.include_router(auth.router) 


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + Docker!"}

@app.post("/name")
def read_name(name: str):
    return {"message": {name}}

# @app.post("/users")
# def create_user(user: models.User):
#     db_user = crud.create_user(db, user)
#     return db_user
