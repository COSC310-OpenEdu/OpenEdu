from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQuery import DatabaseQuery
import os

class DeleteCourseFile(DatabaseQuery):
    @classmethod
    def delete_file_record(cls, file_id):
        try:
            cursor = DatabaseManager.getDatabaseCursor()

            # Retrieve the file path before deletion
            cursor.execute("SELECT fileLocator FROM CourseFiles WHERE fileId = %s", (file_id,))
            file_path = cursor.fetchone()[0]

            # Delete the file record
            cursor.execute("DELETE FROM CourseFiles WHERE fileId = %s", (file_id,))
            DatabaseManager.commit()

            # Check if the file exists and delete it from the filesystem
            if os.path.exists(file_path):
                os.remove(file_path)

            DatabaseManager.closeConnection()
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False

