from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DeleteSolutions(DatabaseUpdate):
    @classmethod 
    def update(cls, dataTuple):
        delete = "DELETE FROM Solution WHERE courseId=%s and assignmentId=%s and studentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(delete, (dataTuple));
        
            
        DatabaseManager.commit();