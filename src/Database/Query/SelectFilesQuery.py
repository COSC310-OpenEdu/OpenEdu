from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQuery import DatabaseQuery

class SelectFilesQuery(DatabaseQuery):
    @classmethod
    def get_files_for_course(cls, courseId):
        query = "SELECT fileId, fileLocator, fileName FROM CourseFiles WHERE courseId = %s"
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(query, (courseId,))
        files = [{'fileId': row[0], 'fileLocator': row[1], 'fileName': row[2]} for row in cursor.fetchall()]
        DatabaseManager.closeConnection()
        return files



class RetrieveFileInfoQuery(DatabaseQuery):
    @classmethod
    def get_file_info(cls, file_id):
        query = "SELECT fileLocator FROM CourseFiles WHERE fileId = %s"
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(query, (file_id,))
        file_info = cursor.fetchone()
        DatabaseManager.closeConnection()
        if file_info:
            return {'fileLocator': file_info[0]}
        else:
            return None
