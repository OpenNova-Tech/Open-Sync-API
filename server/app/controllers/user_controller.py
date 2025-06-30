from app.db import db
from app.models.user_model import UserCreate
from bson import ObjectId
import hashlib

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

async def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    result = await db["users"].insert_one(user_dict)
    return str(result.inserted_id)
