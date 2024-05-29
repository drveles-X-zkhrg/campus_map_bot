from fastapi import FastAPI
from app.routers import items

app = FastAPI()

# Подключение маршрутов
app.include_router(items.router)
