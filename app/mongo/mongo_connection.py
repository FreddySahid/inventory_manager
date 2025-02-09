from motor.motor_asyncio import AsyncIOMotorClient
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    """Class to connect to MongoDB"""
    def __init__(self):
        self.MONGO_URI = os.getenv("MONGODB_URL")
        self.DATABASE_NAME = os.getenv("DATA_BASE")
        self.client = None
        self.db = None

    async def connect(self):

        self.client = AsyncIOMotorClient(self.MONGO_URI)
        self.db = self.client[self.DATABASE_NAME]

mongo_db = MongoDB()

async def check_connection():
    try:
        await mongo_db.db.command("ping")
        return True
    except Exception as e:
        return False
    
asyncio.run(mongo_db.connect())

