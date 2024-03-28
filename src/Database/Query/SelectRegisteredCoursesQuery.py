from src.Database.Query.DatabaseQuery import DatabaseQuery;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectRegisteredCourses(DatabaseQuery):
    @classmethod
    def query(cls, dataTuple) -> tuple:
        registeredCourses = "SELECT Attend.CourseId, name, description, session, term FROM Attend JOIN Course ON Attend.CourseId = Course.courseId WHERE studentId = %s"
        studentId = dataTuple
        try:
            cursor = DatabaseManager.getDatabaseCursor()
            cursor.execute(registeredCourses, (studentId,))
            course = cursor.fetchall()
            DatabaseManager.closeConnection()
        except:
            course = "CONNECTION ERROR"
        return course;