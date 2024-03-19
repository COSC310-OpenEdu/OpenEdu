from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectCourseQueryAll(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> list:
        cursor = DatabaseManager.getDatabaseCursor()
        
        sql = "SELECT courseId, name, credits, session, term, startTime, endTime FROM Course;"
        cursor.execute(sql)
        courseData = cursor.fetchall();
        
        DatabaseManager.closeConnection()
        
        return courseData
        