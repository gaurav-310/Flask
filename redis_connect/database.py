import redis
from dotenv import load_dotenv
import os 

load_dotenv()

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')
password =  os.getenv('REDIS_PASSWORD')


redis_client = redis.Redis(host= host, port=port,password = password,decode_responses=True)


def check_redis_connection():
    if redis_client.ping():
        return True
    else: 
        return False