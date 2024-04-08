from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager

class UpdateSolutionEssay:
    @classmethod
    def update(cls, userId, courseId, assignmentId, file_path, essay_text):
        # Implement the logic to insert or update the Solution table with the essay file path
        cursor = DatabaseManager.getDatabaseCursor()
        # Assuming a row exists for each student and assignment combination
        query = "UPDATE Solution SET studentAnswer = %s WHERE studentId = %s AND courseId = %s AND assignmentId = %s"
        # Update Question table with essay text and set longQuestion to 1
        update_query = """
        UPDATE Question 
        SET questionText = %s, longQuestion = 1 
        WHERE courseId = %s AND assignmentId = %s
        """
        try:
            print("Executing query to update Solution table")
            cursor.execute(query, (file_path, userId, courseId, assignmentId))
            print("Executing query to update Question table")
            cursor.execute(update_query, (essay_text, courseId, assignmentId))
            print("Committing transaction")
            DatabaseManager.commit()
            
        except Exception as e:
            print(f"Error updating database: {e}")
        finally:
            print("Closing connection")
            DatabaseManager.closeConnection()
