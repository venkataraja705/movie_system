'''
connect to mongodb as clinet with server credentials
fetch data 
'''

from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    '''
    connect to 
    database with db_name
    to use collection with collection_name
    '''
    def __init__(self, db_name: str, collection_name: str, uri: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    async def insert_document(self, document: dict):
        result = await self.collection.insert_one(document)
        return result.inserted_id

    async def find_documents(self, query: dict):
        documents = await self.collection.find(query).to_list(length=None)
        return documents