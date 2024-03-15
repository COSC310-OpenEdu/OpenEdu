from pythonFiles.Database.Query.DatabaseQuery import DatabaseQuery;
from pythonFiles.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectStudentQuery(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        sql = "SELECT * FROM User WHERE userId = %s"
        
        userId = dataTuple
        if not isinstance(userId, int): #Only allow userId to be an integer
            return None
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(sql, (userId))
        studentData = cursor.fetchone()
        
        DatabaseManager.closeConnection()

        return studentData