from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql


class SelectStudentQueryAll(DatabaseQueryAll):
    
    #
    #   Gets the students first and last name for all students
    #   Input:  dataTuple = N/A
    #   Ouput:  A list of student names
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
        cursor = DatabaseManager.getDatabaseCursor();
        
        statement = "SELECT firstName, lastName from User"
        cursor.execute(statement)
        studentData = cursor.fetchall()
        
        DatabaseManager.closeConnection();
        
        return studentData