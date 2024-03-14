from DatabaseQuery import DatabaseQuery
from DatabaseManager import DatabaseManager

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