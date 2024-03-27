from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class AddCourseRequest(DatabaseUpdate):
    
    #
    #   Adds a course request for a user in a given course
    #   If a request already exisits do nothing
    #   Input: dataTuple = (studentId, courseId)
    #                    = The student and course being requested
    #
    
    @classmethod
    def update(cls, dataTuple):
        
        sql = "INSERT IGNORE INTO CourseRequests (studentId, courseId) VALUES (%s, %s);"
        
        cursor = DatabaseManager.getDatabaseCursor()
        
        cursor.execute(sql, dataTuple)
        
        DatabaseManager.commit();
        