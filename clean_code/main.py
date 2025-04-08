# internal
# what i wrote
from lib.create_user import handle_create_user

# external
# dependency functions
from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr
# pydantic objects like a java class and BaseModel is like Objects class of Java

# built-in
class User(BaseModel):
    name: str
    email: EmailStr
    # ensures typesafety as well

class UserOutput(BaseModel):
    id: int
    name: str
    email: EmailStr
app: FastAPI = FastAPI() #type hinting
users: list[User] = []
counter: int = 0
@app.post("/user", response_model=UserOutput, status_code=201)
#response model is used for the fastapi documentation to find useroutput and find successful output code is 201
async def create_user(user: User) -> UserOutput:
    return handle_create_user(user)
@app.get("/users", response_model=list[User], status_code=200)
def get_all_users() -> list[User]:
    return users