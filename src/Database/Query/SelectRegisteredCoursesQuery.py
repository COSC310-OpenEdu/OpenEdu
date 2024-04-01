from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectRegisteredCourses(DatabaseQueryAll):
    
    #
    #   Returns all courses for a given student
    #   Input:  dataTuple = (studentId,)
    #                     = The given student
    #   Output: courses   = [[courseId, name, description, session, term]]
    #                     = A list of registered courses
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> list:
        registeredCourses = "SELECT Attend.CourseId, name, description, session, term FROM Attend JOIN Course ON Attend.CourseId = Course.courseId WHERE studentId = %s"
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(registeredCourses, dataTuple)
        courses = cursor.fetchall()
        DatabaseManager.closeConnection()
        
        return courses;