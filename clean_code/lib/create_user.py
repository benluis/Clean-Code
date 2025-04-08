# internal
from main import users, user_counter
from main import User, UserOutput

# external
from pydantic import EmailStr
from fastapi import HTTPException

# built in

async def handle_create_user(user: User) -> UserOutput:
    check_duplicate_email(user.email)
    return create_new_user_record(user.name, user.email)


def check_duplicate_email(email: EmailStr) -> None:
    if any(existing.email == email for existing in users):
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )
    
def create_new_user_record(name: str, email: EmailStr) -> UserOutput:
    global user_counter
    new_user = UserOutput(id=user_counter, name=name, email=email)
    user_counter += 1
    users.append(new_user)
    return new_user