from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DenyCourseRequest(DatabaseUpdate):
    
    #
    #   Denies a course request for a given user
    #   If a request already exisits do nothing
    #   Input: dataTuple = (studentId, courseId)
    #                    = The student and course being approved
    #
    
    @classmethod
    def update(cls, dataTuple):
        
        sql = "Update CourseRequests Set denied = 1 WHERE studentId = %s AND courseId = %s"
        
        cursor = DatabaseManager.getDatabaseCursor()
        
        cursor.execute(sql, dataTuple)
        
        DatabaseManager.commit();
        