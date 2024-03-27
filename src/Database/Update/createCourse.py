from src.Database.DatabaseManager import DatabaseManager

class CreateCourse:
    @classmethod 
    def update(cls, courseData):
        insertCourseSQL = "INSERT INTO Course (name, description, credits, session, term, day, startTime, endTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(insertCourseSQL, courseData)
        DatabaseManager.commit()

