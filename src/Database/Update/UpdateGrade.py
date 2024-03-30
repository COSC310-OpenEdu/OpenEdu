from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class UpdateGrade(DatabaseUpdate):
    @classmethod 
    def update(cls, dataTuple):
        updateGrade = "UPDATE Grades SET grade=%s WHERE courseId=%s and questionId=%s and assignmentId = %s and studentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(updateGrade, (dataTuple));