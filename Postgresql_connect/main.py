
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from crud import create_user, get_users
import asyncio
from fastapi import FastAPI,Depends
from database import engine, Base

app = FastAPI()
@app.get("/")
def index():
	return {"data": "Hello World"}

@app.post("/users/")
async def add_user(name: str, email: str, db: AsyncSession = Depends(get_db)):
    return await create_user(db, name, email)

@app.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await create_tables()
