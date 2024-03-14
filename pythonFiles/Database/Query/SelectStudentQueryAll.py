from DatabaseManager import DatabaseManager
from DatabaseQueryAll import DatabaseQueryAll

class SelectStudentQueryAll(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
        cursor = DatabaseManager.getDatabaseCursor();
        
        statement = "SELECT firstName, lastName from User"
        cursor.execute(statement)
        studentData = cursor.fetchall()
        
        DatabaseManager.closeConnection();
        
        return studentData