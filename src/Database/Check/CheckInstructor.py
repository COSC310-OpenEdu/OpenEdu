from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager

import mysql

class CheckInstuctor(DatabaseCheck):
    
    #
    #   Checks if a given user exists
    #   Input:  dataTuple = (userId,)
    #   Output: True if the user exists
    #
    
    @classmethod
    def check(cls, dataTuple) -> bool:
        cursor = DatabaseManager.getDatabaseCursor()
        
        sql = "SELECT COUNT(userId) FROM Instructor where userId = %s"
        cursor.execute(sql, dataTuple)
        
        return cursor.fetchone()[0] != 0