from src.Database.DatabaseManager import DatabaseManager

class CreateCourse:
    @classmethod 
    def update(cls, courseData, instructorId):
        insertCourseSQL = "INSERT INTO Course (name, description, credits, session, term) VALUES (%s, %s, %s, %s, %s)"
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(insertCourseSQL, courseData)

        courseId = cursor.lastrowid #Get courseid from database

        #Assign professor to teach course
        cursor2 = DatabaseManager.getDatabaseCursor()
        statement2 = "INSERT INTO Instructs(instructorId, courseId) VALUES(%s, %s)"
        cursor2.execute(statement2, (instructorId, courseId))
        DatabaseManager.commit()

