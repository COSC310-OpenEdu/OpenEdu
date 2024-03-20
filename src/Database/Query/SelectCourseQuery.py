from src.Database.Query.DatabaseQuery import DatabaseQuery;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectCourseQuery(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        getCourseName = "SELECT Instructs.courseId, name FROM Instructs JOIN Course ON Course.courseId = Instructs.courseId WHERE instructorId  = %s"

        instructorId = dataTuple
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(getCourseName, (instructorId))
        course = cursor.fetchall()
        DatabaseManager.closeConnection()
        
        return course;
        