from src.Database.Query.DatabaseQuery import DatabaseQuery;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectStudentQuery(DatabaseQuery):
    
    #
    #   Gets student information 
    #   Input: dataTuple = (userId,)
    #   Ouput: The student's data
    #
    
    @classmethod
    def query(cls, dataTuple) -> tuple:
        sql = "SELECT * FROM User WHERE userId = %s"
        
        userId = dataTuple[0];
        if not isinstance(userId, int): #Only allow userId to be an integer
            return None
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(sql, (userId,))
        studentData = cursor.fetchone()
        
        DatabaseManager.closeConnection()

        return studentData