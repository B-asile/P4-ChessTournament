from tinydb import TinyDB, Query
from datetime import datetime

class DB:
    db = TinyDB('stored_data.json')
    table_tournaments = db.table('Tournament')
    table_players = db.table('Player')
    table_matchs = db.table('Matchs')

    def __init__(self, table):
        self.table = table


    @staticmethod
    def TinyDBDropTables():
        DB.db.drop_tables()



