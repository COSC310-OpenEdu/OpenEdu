from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class DenyCourseRequest(DatabaseUpdate):
    
    #
    #   Removes a course request for a given student
    #   If a request already exisits do nothing
    #   Input: dataTuple = (studentId, courseId)
    #                    = The student and course being approved
    #
    
    @classmethod
    def update(cls, dataTuple):
        
        sql = "DELETE FROM CourseRequests WHERE studentId = %s AND courseId = %s"
        
        cursor = DatabaseManager.getDatabaseCursor()
        
        cursor.execute(sql, dataTuple)
        
        DatabaseManager.commit();
        