from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectCourseQueryAll(DatabaseQueryAll):
    
    #
    #   Selects courses with names that contain the input
    #   Input:  dataTuple = (searchTerm)
    #   Ouput:  A list of courses
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> list:
        cursor = DatabaseManager.getDatabaseCursor()
    
        sql = "SELECT courseId, name, credits, session, term, startTime, endTime FROM Course WHERE name LIKE %s;"
        cursor.execute(sql, ("%" + dataTuple[0] + "%",))
        courseData = cursor.fetchall();
        
        DatabaseManager.closeConnection()
        print(courseData)
        return courseData
        