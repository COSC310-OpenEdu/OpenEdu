from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class SubmitAssignment(DatabaseUpdate):

    #
    # Submits a question into the Solutions table.
    # Input : dataTuple = (courseId, questionId, assignmentId, studentId, studentAnswer)
    # Output : N/A
    #

    @classmethod 
    def update(cls, dataTuple):
        submitAssignment = "INSERT INTO Solution VALUES (%s, %s, %s, %s, %s)"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(submitAssignment, (dataTuple));
        
            
