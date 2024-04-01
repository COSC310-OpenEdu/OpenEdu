from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DeleteSolutions(DatabaseUpdate):

    #
    # Deletes a submission for a student. Can only be used if grades do not exist for that submission
    # Input : dataTuple = (courseId, assignmentId, studentId)
    # Output : N/A
    #

    @classmethod 
    def update(cls, dataTuple):
        delete = "DELETE FROM Solution WHERE courseId=%s and assignmentId=%s and studentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(delete, (dataTuple));
        
            
