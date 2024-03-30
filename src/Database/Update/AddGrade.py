from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class AddGrade(DatabaseUpdate):
    @classmethod 
    def update(cls, dataTuple):
        addGrade = "INSERT INTO Grades VALUES (%s, %s, %s, %s, %s, %s, null)"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(addGrade, (dataTuple));
        
            
        DatabaseManager.commit();