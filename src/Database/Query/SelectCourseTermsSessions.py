from src.Database.DatabaseManager import DatabaseManager

class SelectCourseTermsSessions:
    @staticmethod
    def get_sessions():
        try:
            cursor = DatabaseManager.getDatabaseCursor()
            cursor.execute("SELECT DISTINCT session FROM Course")
            return {row[0]: 'Fall' if row[0] == 1 else 'Winter' for row in cursor.fetchall()}
        except Exception as e:
            print(f"Database error: {e}")
            return {}

    @staticmethod
    def get_terms():
        try:
            cursor = DatabaseManager.getDatabaseCursor()
            cursor.execute("SELECT DISTINCT term FROM Course")
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(f"Database error: {e}")
            return []
