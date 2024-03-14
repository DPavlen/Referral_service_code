from fastapi import FastAPI
from app.users.router import router_auth


app = FastAPI(
    title="API сервис для реферальной системы",
)

app.include_router(router_auth)

@app.get("/code")
def get_hello():
    return "API сервис для реферальной системы"