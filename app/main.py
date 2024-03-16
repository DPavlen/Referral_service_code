import sys
import os


from fastapi import FastAPI
from users.router import router

app = FastAPI(
    title="API сервис для реферальной системы",
)

app.include_router(router)


# @app.get("/code")
# def get_hello():
#     return "API сервис для реферальной системы"
