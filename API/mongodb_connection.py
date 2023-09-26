from pymongo import MongoClient
import certifi

def mongo_connection():
    mongo_uri = "mongodb+srv://azadchauhan012654:1TwDsLpOD0zrmVVW@cluster0.d9cwhmf.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(mongo_uri,tlsCAFile=certifi.where())
    db = client['resumeDB'] 
    # collection = db['personal_data']
    return db



