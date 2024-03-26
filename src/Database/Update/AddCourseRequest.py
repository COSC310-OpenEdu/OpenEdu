from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class AddCourseRequest(DatabaseUpdate):
    
    @classmethod
    def update(cls, dataTuple):
        
        sql = "INSERT IGNORE INTO CourseRequests (studentId, courseId) VALUES (%s, %s);"
        
        cursor = DatabaseManager.getDatabaseCursor()
        
        cursor.execute(sql, dataTuple)
        
        DatabaseManager.commit();
        