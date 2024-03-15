from pythonFiles.Database.Query.DatabaseQuery import DatabaseQuery;
from pythonFiles.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectCourseQuery(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        getCourseName = "SELECT name FROM Course WHERE courseId  = %s"

        courseId = dataTuple
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(getCourseName, (courseId))
        course = cursor.fetchone()
        DatabaseManager.closeConnection()
        
        return course;
        