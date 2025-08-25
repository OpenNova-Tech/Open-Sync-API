from fastapi import APIRouter
from app.db import db
from app.models.user_model import UserCreate
from app.controllers.user_controller import create_user

router = APIRouter()

def serialize_user(user):
    user["_id"] = str(user["_id"])
    return user

@router.get("/")
async def get_users():
    users = await db["users"].find().to_list(10)
    return {"users": [serialize_user(user) for user in users]}

@router.post("/users")
async def register_user(user: UserCreate):
    user_id = await create_user(user)
    return {"message": "User created", "user_id": user_id}
