from src.Database.Query.DatabaseQuery import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectCourseQuery(DatabaseQueryAll):
    
    #
    #   Returns courses that an Instructor instructs
    #   Input: dataTuple = (instructorId,)
    #   Ouput: A list of courses
    #
    
    @classmethod
    def query(cls, dataTuple) -> list:
        getCourseName = "SELECT Instructs.courseId, name, description FROM Instructs JOIN Course ON Course.courseId = Instructs.courseId WHERE instructorId  = %s"
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(getCourseName, dataTuple)
        course = cursor.fetchall()
        DatabaseManager.closeConnection()
        
        return course;
        