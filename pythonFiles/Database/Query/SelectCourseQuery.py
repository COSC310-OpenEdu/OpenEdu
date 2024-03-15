from DatabaseQuery import DatabaseQuery;
from DatabaseManager import DatabaseManager;

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
        