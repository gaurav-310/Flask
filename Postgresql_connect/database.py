from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os


DATABASE_URL = "postgresql+asyncpg://gauravtripathi:gaur%409899@localhost:5432/Post"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# import to start the session 
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
