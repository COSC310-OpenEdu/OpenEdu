from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class SubmitAssignment(DatabaseUpdate):
    @classmethod 
    def update(cls, dataTuple):
        submitAssignment = "INSERT INTO Solution VALUES (%s, %s, %s, %s, %s)"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(submitAssignment, (dataTuple));
        
            
        DatabaseManager.commit();