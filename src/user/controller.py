from src.user.dtos import UserSchema
from sqlalchemy.orm import Session


def register(body, db):
    print(body)
    return{ "msg": "registration done"}