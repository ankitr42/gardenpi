from tinydb import TinyDB

from consts import LOG_FILE_PATH

db = TinyDB(LOG_FILE_PATH)

def insertEntry(entry):
    db.insert(entry)
    
def getLatestEntry():
    return db.all()[-1]
