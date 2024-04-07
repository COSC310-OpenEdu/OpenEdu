from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DeleteAllQuestionsForAssignment(DatabaseUpdate):

    #
    # Deletes all questions for an assignment.
    # Input: dataTuple = (courseId, assignmentId)
    # Output: N/A
    #

    @classmethod 
    def update(cls, dataTuple):
        delete = "DELETE FROM Question WHERE courseId=%s and assignmentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(delete, (dataTuple));