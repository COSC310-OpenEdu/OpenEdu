from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DeleteAllSolutionsForAssignment(DatabaseUpdate):

    #
    # Deletes all solutions for an assignment. Designed to be worked in conjuction with DeleteGradesForAssignment
    # and DeleteAssignment
    # Input: dataTuple = (courseId, assignmentId)
    # Output: N/A
    #

    @classmethod 
    def update(cls, dataTuple):
        delete = "DELETE FROM Solution WHERE courseId=%s and assignmentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(delete, (dataTuple));
        
            
     