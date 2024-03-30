from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckStudent(DatabaseCheck):
    
    #
    #   Checks if a given student exists
    #   Input:  dataTuple = (userId,)
    #   Output: True if the student exists
    #
    
    @classmethod
    def check(cls, dataTuple) -> bool:
        cursor = DatabaseManager.getDatabaseCursor()
        
        sql = "SELECT COUNT(userId) FROM Student where userId = %s"
        cursor.execute(sql, dataTuple)
        
        return cursor.fetchone()[0] == 1