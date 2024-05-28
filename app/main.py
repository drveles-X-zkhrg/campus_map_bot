from fastapi import FastAPI
from app.routers import items
from app.database import engine, Base

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение маршрутов
app.include_router(items.router)
