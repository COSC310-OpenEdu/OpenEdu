from pythonFiles.Database.Query.DatabaseQuery import DatabaseQuery
from pythonFiles.Database.DatabaseManager import DatabaseManager
import mysql


class SelectStudentUserPass(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        username, password = dataTuple;
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (username,password))
        
        userData = cursor.fetchone()

        DatabaseManager.closeConnection();

        return userData