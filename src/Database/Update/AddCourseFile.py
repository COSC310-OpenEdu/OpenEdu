from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQuery import DatabaseQuery

class AddCourseFile(DatabaseQuery):
    
    #
    #   Inserts information about a file and where it is stored
    #   Input: courseId = the course this file is stored in
    #          file_path = The path the file is store in the file system
    #          file_name = The name of the file in the file system
    #   Output: N/A
    
    @classmethod
    def insert_file_record(cls, courseId, file_path, file_name):
        query = "INSERT INTO CourseFiles (courseId, fileLocator, fileName) VALUES (%s, %s, %s)"
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(query, (courseId, file_path, file_name))
        DatabaseManager.commit()
        DatabaseManager.closeConnection()

