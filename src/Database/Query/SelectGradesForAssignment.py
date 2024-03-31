from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectGradesForAssignment(DatabaseQueryAll):
    
    #
    #   Selects the all questions grades and comments for a given courseId, assignmentId, and studentId
    #   Input:  dataTuple = (courseId, assignmentId, studentId)
    #   Ouput:  A list of questions and grades for the given assignment
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
        getGrades = "SELECT questionId, grade, comment FROM Grades WHERE courseId=%s and assignmentId=%s and studentId=%s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(getGrades, (dataTuple))
        allGrades = cursor.fetchall();
        DatabaseManager.closeConnection();
        
        return allGrades