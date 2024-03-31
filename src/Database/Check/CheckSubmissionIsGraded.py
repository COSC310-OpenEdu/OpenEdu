from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CheckSubmissionIsGraded(DatabaseCheck):

    #
    # Checks if a submission has been graded.
    # Input : dataTuple = (courseId, assignmentId, studentId)
    # Output : False if no grade exists. True if it does.
    #

    @classmethod
    def check(self, dataTuple):
        statement = "SELECT questionId FROM Grades WHERE courseId=%s and assignmentId=%s and studentId=%s"

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (dataTuple))
        grades = cursor.fetchall()
        DatabaseManager.closeConnection();
    
        if grades is None:
            return False
        else:
            return True