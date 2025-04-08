# internal 
from lib.create_user import handle_creat_user

# external 
from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr

# built in


class User(BaseModel):
    name: str
    email: EmailStr

class UserOutput(BaseModel):
    id: int
    name: str
    email: EmailStr


app: FastAPI = FastAPI()
users: list[User] = []
user_counter: int = 0

@app.post("/user", response_model=UserOutput, status_code=201)
async def create_user(user: User) -> UserOutput:
    return handle_creat_user(user)

@app.get("/users", response_model=list[User], status_code=200)
def get_all_users() -> list[User]:
    return users