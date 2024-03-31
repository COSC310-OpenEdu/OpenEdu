from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class AddGrade(DatabaseUpdate):

    #
    # Creates a grade for a given question in a submission
    # Input: dataTuple = (courseId, questionId, assignmentId, studentId, intructorId, grade)
    # Output: N/A
    #

    @classmethod 
    def update(cls, dataTuple):
        addGrade = "INSERT INTO Grades VALUES (%s, %s, %s, %s, %s, %s, null)"
        
        cursor = DatabaseManager.getDatabaseCursor();
    
        cursor.execute(addGrade, (dataTuple));
        
            
        