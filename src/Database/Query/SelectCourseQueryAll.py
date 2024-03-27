from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectCourseQueryAll(DatabaseQueryAll):
    # Returns the course information course within the database
    #   Input:  searchTerm = A search term that the database will compare the name to
    #                        If this is None then the database will return all values
    
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
        