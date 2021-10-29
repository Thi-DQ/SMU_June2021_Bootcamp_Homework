import pymongo

class MongoHelper():
    def __init__(self):
        # Create connection variable
        self.conn = 'mongodb://localhost:27017'

        # Pass connection to the pymongo instance.
        self.client = pymongo.MongoClient(self.conn)

        # Connect to a database. Will create one if not already available.
        self.db = self.client.mars_scraping

    def insertInfo(self, data):
        # insert into mongo
        self.db.mars_info.insert_one(data)
        return({"ok": True})

    def findLastInfo(self):
        scrape_info = self.db.mars_info.find({}, sort=[('last_updated', pymongo.DESCENDING)], limit=1)
        return(scrape_info[0])