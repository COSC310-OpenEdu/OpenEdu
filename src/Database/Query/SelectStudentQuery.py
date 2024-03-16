from src.Database.Query.DatabaseQuery import DatabaseQuery;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectStudentQuery(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        sql = "SELECT * FROM User WHERE userId = %s"
        

        #if not isinstance(userId, int): #Only allow userId to be an integer
        #    return None
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(sql, dataTuple)
        studentData = cursor.fetchone()
        
        DatabaseManager.closeConnection()

        return studentData