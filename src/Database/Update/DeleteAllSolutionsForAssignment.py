from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DeleteAllSolutionsForAssignment(DatabaseUpdate):
    @classmethod 
    def update(cls, dataTuple):
        delete = "DELETE FROM Solution WHERE courseId=%s and assignmentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(delete, (dataTuple));
        
            
        DatabaseManager.commit();