from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class UpdateGrade(DatabaseUpdate):
    
    #
    #   Updates the grade of a question on an assignment
    #   Input:  dataTuple = (grade, courseId, questionId, assignmentId, studentId)
    #   Output: N/A
    #
    
    @classmethod 
    def update(cls, dataTuple):
        updateGrade = "UPDATE Grades SET grade=%s WHERE courseId=%s and questionId=%s and assignmentId = %s and studentId=%s"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(updateGrade, (dataTuple));