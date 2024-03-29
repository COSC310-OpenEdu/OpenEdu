from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
from src.Database.Update.DenyCourseRequest import DenyCourseRequest
import mysql

class ApproveCourseRequest(DatabaseUpdate):
    
    #
    #   Approves the course request for the given student
    #   The course request is then removed from the database
    #   If a request already exisits do nothing
    #   Input: dataTuple = (studentId, courseId)
    #                    = The student and course being approved
    #
    
    @classmethod
    def update(cls, dataTuple):
        
        # approve the request
        sql = "INSERT IGNORE INTO Attend (studentId, courseId) VALUES (%s, %s);"    
        cursor = DatabaseManager.getDatabaseCursor()     
        cursor.execute(sql, dataTuple)
        
        # Remove the student's request from the database
        DenyCourseRequest.update(dataTuple);
        
        DatabaseManager.commit();
        