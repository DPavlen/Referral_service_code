import sys
import os


from fastapi import FastAPI
from users.router import router

app = FastAPI(
    debug=True,
    title="API сервис для реферальной системы",
)

app.include_router(router)