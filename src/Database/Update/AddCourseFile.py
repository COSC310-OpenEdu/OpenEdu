from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQuery import DatabaseQuery

class AddCourseFile(DatabaseQuery):
    @classmethod
    def insert_file_record(cls, courseId, file_path, file_name):
        query = "INSERT INTO CourseFiles (courseId, fileLocator, fileName) VALUES (%s, %s, %s)"
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(query, (courseId, file_path, file_name))
        DatabaseManager.commit()
        DatabaseManager.closeConnection()

