from os import getenv
from dotenv import load_dotenv
from models import *
from mongoengine import connect
import crud as crud
from typing import List
from fastapi import Body, FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse

load_dotenv()

connect(host=getenv("DB_URI"))

app = FastAPI()


@app.post("/users")
async def create_user(user: UserCreate = Body(...)):
    new_user = crud.create_user(name=user.name)
    return {"message": "User created successfully", "user_id": str(new_user.id)}


@app.get("/users/{user_id}", response_model=UserModel)
async def read_user(user_id: str = Path(..., regex=r"^[0-9a-f]{24}$")):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_json = user.to_json()
    return JSONResponse(content=user_json)


@app.delete("/users/{user_id}")
async def delete_user(user_id: str = Path(..., regex=r"^[0-9a-f]{24}$")):
    success = crud.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully", "user_id": str(user_id)}


@app.get("/users", response_model=List[UserModel])
async def read_users():
    users = crud.get_all_users()
    users_json = users.to_json()
    return JSONResponse(content=users_json)
