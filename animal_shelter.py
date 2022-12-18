from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        
        # self.client = MongoClient(['mongodb://localhost:55766'])  # Initializing MongoDB client WITHOUT authentication
        
        self.client = MongoClient('mongodb://%s:%s@localhost:55766' % (username, password))  # Initializing MongoDB client WITH authentication
        
        self.database = self.client['AAC']
        
        
             # C
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save because data parameter is empty")

             # R
    def read(self, data):
        cursor = self.database.animals.find(data, {"_id": False})
        
        return cursor # Return cursor object to be able to call for M6
        
    
    
            # U
    def update(self, data, updatedData):
        if data is not None:
            updated_Data = self.database.animals.update_many(data, updatedData)
            
            return dumps(self.read(updatedData))
        else:
            raise Exception("Nothing to update because data parameter is empty")
            return false
        
           # D
    def delete(self, data):
        if data is not None:
            deleted_Data = self.database.animals.delete_many(data)
            return dumps(self.read(data))
        else:
            raise Exception("Nothing to delete because data parameter is empty")
            return false