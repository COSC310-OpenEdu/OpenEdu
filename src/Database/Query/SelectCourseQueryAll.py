from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectCourseQueryAll(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> list:
        cursor = DatabaseManager.getDatabaseCursor()
        
        searchTerm = dataTuple[0];
        if (searchTerm == None): 
            sql = "SELECT courseId, name, description, credits, session, term, startTime, endTime FROM Course;"
            cursor.execute(sql)
        else:
            searchTerm =  '%' + searchTerm + '%'
            sql = "SELECT courseId, name, description, credits, session, term, startTime, endTime FROM Course WHERE name LIKE %s;"
            cursor.execute(sql, (searchTerm,))
        
        courseData = cursor.fetchall();
        
        DatabaseManager.closeConnection()
        
        return courseData
        