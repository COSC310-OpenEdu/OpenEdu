from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectRequestableCourses(DatabaseQueryAll):
    # Returns the course information course that a given users is not enrolled in and a boolean if the course is requested alread
    #   Input:  dataTuple = (searchTerm, user)
    #                     = 
    
    @classmethod
    def queryAll(cls, dataTuple) -> list:
        cursor = DatabaseManager.getDatabaseCursor()
        
        searchTerm = dataTuple[0]
        studentId = dataTuple[1]
        
        searchTerm = dataTuple[0];
        if (searchTerm == None): 
            sql = "SELECT UNIQUE C.courseId, C.name, C.description, C.credits, C.session, C.term, C.startTime, C.endTime,(SELECT COUNT(courseId) FROM CourseRequests AS CR WHERE CR.courseId = C.courseId AND CR.studentId = %s) AS Requested FROM Course AS C WHERE C.courseId NOT IN (SELECT courseId FROM Attend WHERE studentId = %s)"
            cursor.execute(sql, (studentId, studentId))
        else:
            searchTerm =  '%' + searchTerm + '%'
            sql = "SELECT UNIQUE C.courseId, C.name, C.description, C.credits, C.session, C.term, C.startTime, C.endTime,(SELECT COUNT(courseId) FROM CourseRequests AS CR WHERE CR.courseId = C.courseId AND CR.studentId = %s) AS Requested FROM Course AS C WHERE C.courseId NOT IN (SELECT courseId FROM Attend WHERE studentId = %s) AND (C.name LIKE %s OR C.description LIKE %s);"
            cursor.execute(sql, (studentId, studentId, searchTerm, searchTerm))
        
        courseData = cursor.fetchall();
        
        DatabaseManager.closeConnection()
        
        return courseData
        