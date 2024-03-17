from fastapi import FastAPI

from app.users.router import router

app = FastAPI(
    debug=True,
    title="API сервис для реферальной системы",
)

app.include_router(router)
