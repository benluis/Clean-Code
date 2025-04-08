# internal
from main.py import users, user_counter
from main.py import User, UserOutput

# external
from fastapi import HTTPException
from pydantic import EmailStr

# built-in

def handle_create_user(user: User) -> UserOutput:
    check_duplicate_email(user.email)
    return create_new_user_record(user.name, user.email)

def check_duplicate_email(email: EmailStr) -> None:
    if any(existing.email == email for existing in users):
        raise HTTPException(status_code = 400, detail="Email already exists")

def create_new_user_record(name: str, email: EmailStr) -> UserOutput:
    global user_counter
    new_user = UserOutput(id=user_counter, name=name, email=email)
    user_counter += 1
    users.append(new_user)
    return new_user