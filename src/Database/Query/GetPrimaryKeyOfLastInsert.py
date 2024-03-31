from src.Database.Query.DatabaseQuery import DatabaseQuery
from src.Database.DatabaseManager import DatabaseManager
import mysql

class GetPrimaryKeyOfLastInsert(DatabaseQuery):
    
    #
    #   Returns the primary key of the last insert
    #   Input: N/A
    #   Ouput: The key
    #
    
    @classmethod
    def query(cls, dataTuple) -> tuple:
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
        
        return cursor.fetchone();