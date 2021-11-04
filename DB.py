from tinydb import TinyDB, Query
from datetime import datetime
# from tinydb_serialization import Serializer


# class DateTimeSerializer(Serializer):
#     DateTimeSerializer = datetime  # The class this serializer handles
#     return obj.isoformat()
#
#     def decode(self, s):
#         return datetime.fromisoformat(s)

class DBcls:
    db = TinyDB('DB.json')
    table_tournaments = db.table('Tournamentcls')
    table_players = db.table('Playercls')

    def __init__(self, table):
        self.table = table


    @staticmethod
    def TinyDBDropTables():
        DBcls.db.drop_tables()



