from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DeleteAssignment(DatabaseUpdate):

    #
    # Deletes an assignment. Designed to be used in conjunction with DeleteAllSolutionsForAssignment and
    # DeleteGradesForAssignment
    # Input : dataTuple = (courseId, assignmentId)
    # Output : N/A
    #

    @classmethod 
    def update(cls, dataTuple):
        delete = "DELETE FROM Assignment WHERE courseId=%s and assignmentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(delete, (dataTuple));
        
            
       