from fastapi import FastAPI
from src.models import User

app = FastAPI()

users = []
@app.post("/auth/register")
async def register(user:User):
    for us in users:
        if us["username"] == user.username:
            return {"message":"Пользователь уже зарегестрирован!"}
    users.append({"username": user.username,
                "password":user.password})
    return {"message":"Пользователь успешно зарегестрирован!"}