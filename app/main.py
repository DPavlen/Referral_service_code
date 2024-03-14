from fastapi import FastAPI



app = FastAPI(
    title="API сервис для реферальной системы",
    version="0.1.0",
    openapi_tags="Referral_service_code",
)
@app.get("/code")
def get_hello():
    return "API сервис для реферальной системы"