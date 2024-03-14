from DatabaseQuery import DatabaseQuery;
from DatabaseManager import DatabaseManager;

class QuertSelectStudent(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        userId = dataTuple;
        if not isinstance(userId, int): #Only allow userId to be an integer
            return None
        
        statement = "SELECT * FROM User WHERE userId = %s"
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (userId,))
        studentData = cursor.fetchone()
        
        DatabaseManager.closeConnection()

        return studentData