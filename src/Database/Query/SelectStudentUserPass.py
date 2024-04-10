from src.Database.Query.DatabaseQuery import DatabaseQuery
from src.Database.DatabaseManager import DatabaseManager
import mysql


class SelectStudentUserPass(DatabaseQuery):
    
    #
    #   Gets user information from username and password
    #   Input: dataTuple = (username, password)
    #   Output: infromation about the selected user
    #
    
    @classmethod
    def query(cls, dataTuple) -> tuple:
        username, password = dataTuple;
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (username,password))
        
        userData = cursor.fetchone()

        DatabaseManager.closeConnection();

        return userData