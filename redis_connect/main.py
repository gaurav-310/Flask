from fastapi import FastAPI
from database import redis_client, check_redis_connection  # Import Redis client
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    return {"response": "Hello World"}

@app.get("/redis")
async def index():
    if check_redis_connection():
        
        return {"response": "Redis connected successfully"}
    else:
        return {"response": "Redis connection failed"}


if __name__ == "__main__":
    
    uvicorn.run(app, port = 8000)