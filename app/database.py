from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://mongo:27017"
DB_NAME = "academia"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
