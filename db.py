from tinydb import TinyDB, Query
from datetime import datetime
# from tinydb_serialization import Serializer


# class DateTimeSerializer(Serializer):
#     DateTimeSerializer = datetime  # The class this serializer handles
#     return obj.isoformat()
#
#     def decode(self, s):
#         return datetime.fromisoformat(s)

class DB:
    db = TinyDB('db.json')
    table_tournaments = db.table('Tournament')
    table_players = db.table('Player')
    table_matchs = db.table('Matchs')

    def __init__(self, table):
        self.table = table


    @staticmethod
    def TinyDBDropTables():
        DB.db.drop_tables()



